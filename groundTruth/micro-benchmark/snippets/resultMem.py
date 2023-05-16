import os


def getMem(pycgPath,pythonPath):
    pycgmem = 0
    pythonmem = 0
    with open(pycgPath,'r') as f:
        lines = f.read().split('\n')
    for line in lines:
        line = line.strip()
        # print(line)
        if line.endswith("maximum resident set size"):
            res = line.replace("maximum resident set size",'')
            res = int(res)
            pycgmem = res
    with open(pythonPath,'r') as f:
        lines = f.read().split('\n')
    for line in lines:
        line = line.strip()
        # print(line)
        if line.endswith("maximum resident set size"):
            res = line.replace("maximum resident set size",'')
            res = int(res)
            pythonmem = res      
            break
    return pycgmem,pythonmem
def findFile(base):
    for root, ds, fs in os.walk(base):
        returnList = [0] * 2
        pycgPath,pythonPath = None,None
        for f in fs:
            if f == 'pycg.log':
                pycgPath = os.path.join(root, f)
            if f == 'pythoncg.log':
                pythonPath = os.path.join(root, f)
        # yield run(returnList[0] , returnList[1] , returnList[2])
        yield getMem(pycgPath,pythonPath)
        # main(returnList[0] , returnList[1]  ,returnList[2])
def process(pycg_list , pythoncg_list):
    pre_pycg = [0,0,0,0]
    pre_python = [0,0,0,0]
    pre_pycg = list(map(lambda x:x[0] + x[1] , zip(pre_pycg,pycg_list)))
    yield pre_pycg
global_pycg = 0
global_pythoncg = 0
def main(base):
    global global_pycg
    global global_pythoncg
    pre_pycg = 0
    pre_python = 0
    for root, ds, fs in os.walk(base):
        returnList = [0] * 2
        pycgPath,pythonPath = None,None
        for f in fs:
            if f == 'pycg.log':
                pycgPath = os.path.join(root, f)
            if f == 'pythoncg.log':
                pythonPath = os.path.join(root, f)
        # yield run(returnList[0] , returnList[1] , returnList[2])
        yield getMem(pycgPath,pythonPath)
    # for i in findFile(base):
    #     if not i:
    #         continue
    #     pre_pycg = list(map(lambda x:x[0] + x[1] , zip(pre_pycg,list(i[0]))))
    #     pre_python = list(map(lambda x:x[0] + x[1] , zip(pre_python,list(i[1]))))
        # print(pre_pycg,pre_python)
    pycg_str = "{},{},{}/{}".format(*pre_pycg)
    python_str = "{},{},{}/{}".format(*pre_python)
    res = pre_pycg + pre_python
    # save_xlsx(190+index,base.split(os.path.sep)[-1],res)
    print(base.split(os.path.sep)[-1])
    print(pycg_str , python_str)
    global_pycg = list(map(lambda x:x[0] + x[1] , zip(pre_pycg,global_pycg)))
    global_pythoncg = list(map(lambda x:x[0] + x[1] , zip(pre_python,global_pythoncg)))


SNIPPETS_PATH = "/Users/yixuanyan/yyx/github/supplychain/YanYixuan/pythonCG/micro-benchmark/snippets"
entries = [
    f"{SNIPPETS_PATH}/assignments",
    f"{SNIPPETS_PATH}/builtins",
    f"{SNIPPETS_PATH}/classes",
    f"{SNIPPETS_PATH}/decorators",
    f"{SNIPPETS_PATH}/dicts",
    f"{SNIPPETS_PATH}/direct_calls",
    f"{SNIPPETS_PATH}/exceptions",
    f"{SNIPPETS_PATH}/functions",
    f"{SNIPPETS_PATH}/generators",
    f"{SNIPPETS_PATH}/imports",
    f"{SNIPPETS_PATH}/kwargs",
    f"{SNIPPETS_PATH}/lambdas",
    f"{SNIPPETS_PATH}/lists",
    f"{SNIPPETS_PATH}/mro",
    f"{SNIPPETS_PATH}/args",
    f"{SNIPPETS_PATH}/returns",
    # New cases
    f"{SNIPPETS_PATH}/newCase/args",
    f"{SNIPPETS_PATH}/newCase/assign",
    f"{SNIPPETS_PATH}/newCase/calls",
    f"{SNIPPETS_PATH}/newCase/control_flow",
    f"{SNIPPETS_PATH}/newCase/import",
]
pycgtotal =0
pythontotal = 0
for index,entry in enumerate(entries):
    print(entry.split(os.path.sep)[-1])
    visited = set()
    pycgcur ,pythoncur = 0,0
    for root, ds, fs in os.walk(entry):
        pycgPath, pythonPath = None, None
        for f in fs:
            if f == 'pycg.log':
                pycgPath = os.path.join(root, f)
            if f == 'pythoncg.log':
                pythonPath = os.path.join(root, f)
            if pycgPath and pythonPath and (pycgPath,pythonPath) not in visited:
                pyT ,pythonT =  getMem(pycgPath, pythonPath)
                visited.add((pycgPath,pythonPath))
                pycgcur , pythoncur = pycgcur + pyT , pythoncur + pythonT
    pycgtotal , pythontotal = pycgtotal + pycgcur , pythoncur + pythontotal
    print(round(pycgcur/(1024**2)),round(pythoncur/(1024**2)))
print(round(pycgtotal/(1024**2)),round(pythontotal/(1024**2)))