import sys

data = []
headers = []

for line in open('original_data.csv'):
    items = line.rstrip().split(',')

    datum = {}
    if items[0] =='action_type':
        headers  = items
    else:
        for i in range(len(headers)):
            header = headers[i]
            datum[header] = items[i]
        data.append(datum)

sst = {}  # specific shot type
ast = {}  # all shot types

ave_sst = {'Bank Shot':0.792, 'Dunk':0.928, 'Hook Shot':0.535, 'Jump Shot':0.391, 'Layup': 0.565, 'Tip Shot': 0.349}
ave_ast = 0.446

for datum in data:
    if len(datum['shot_made_flag']) ==0: continue

    shot_type = datum['combined_shot_type']
    eid = datum['game_event_id']

    if eid=='35':
        pass

    if eid not in sst:
        sst[eid] = {}
    if shot_type not in sst[eid]:
        sst[eid][shot_type] = {}
        sst[eid][shot_type]['in'] = 0
        sst[eid][shot_type]['total'] = 0

    if datum['shot_made_flag'] =='1':
        sst[eid][shot_type]['in'] +=1
    sst[eid][shot_type]['total'] +=1

    if eid not in ast:
        ast[eid] = {}
        ast[eid]['in'] = 0
        ast[eid]['total'] = 0

    if datum['shot_made_flag'] =='1':
        ast[eid]['in'] +=1
    ast[eid]['total'] +=1

print ",".join(headers) +",sst_rate,sst_total,ast_rate,ast_total"

for datum in data:
    shot_type = datum['combined_shot_type']
    eid = datum['game_event_id']

    sst_rate = ave_sst[shot_type]
    sst_total = 0
    ast_rate = ave_ast
    ast_total = 0

    try:
        sst_rate = 1.0* sst[eid][shot_type]['in'] / sst[eid][shot_type]['total']
        sst_total = sst[eid][shot_type]['total']
    except:
        pass

    try:
        ast_rate = 1.0*ast[eid]['in'] / ast[eid]['total']
        ast_total = ast[eid]['total']
    except:
        pass

    outputs = []
    for header in headers:
        outputs.append(datum[header])
    outputs += [sst_rate, sst_total, ast_rate, ast_total]

    print ",".join([str(x) for x in outputs])

        

    
    
