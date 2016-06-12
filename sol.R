setwd("/Users/Asura/Documents/kaggle/kobe_bryant_shot_selection")

data = read.csv("add-fields.csv", header=T)
data$shot_made_flag = factor(data$shot_made_flag)
data$time_remain = data$minutes_remaining*60+data$seconds_remaining

train =  subset(data, !is.na(shot_made_flag))
test =  subset(data, is.na(shot_made_flag))

# the R section is relatively simple given that I already computed the game and type-specific success rate
library("randomForest")

rf1 = randomForest(shot_made_flag~combined_shot_type+ lat+lon+time_remain+period+playoffs+shot_zone_area+shot_distance+team_name+opponent+ sst_rate+sst_total+ast_rate+ast_total, data=train)
# OOB error rate: 39.42%

rf_out = predict(rf1, test, type='prob', norm.votes=F)[,2]
write.table(data.frame(shot_id=test$shot_id, shot_made_flag=rf_out), file='rf_sub.csv', quote=F, sep=',',row.names=F, col.names=T)


library("glmnet")
trainx = as.matrix(train[,c(5,8,10,11,14,26,27,28,29,30)])
trainy = train[,15]
testx = as.matrix(test[,c(5,8,10,11,14,26,27,28,29,30)])
lasso1 = cv.glmnet(trainx, trainy,alpha=1,family='binomial')

# calculated the error to be 0.3592
mean(as.numeric(predict(lasso1, trainx, type='response') >0.5) != trainy)
lasso_out = predict(lasso1, testx, type='response')[,1]
write.table(data.frame(shot_id=test$shot_id, shot_made_flag=lasso_out), file='lasso_sub.csv', quote=F, sep=',',row.names=F, col.names=T)

