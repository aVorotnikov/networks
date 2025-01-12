# Вывод

## Линейная топология
```
topology: linear

dr(0): (MsgType.NEIGHBORS: [1])
dr(0): (MsgType.GET_TOPOLOGY: None)
r(0) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x7ddab8836bf0>)
dr(1): (MsgType.NEIGHBORS: [0, 2])
dr(1): (MsgType.GET_TOPOLOGY: None)
r(0) : (MsgType.NEIGHBORS: {'index': 1, 'neighbors': [0, 2]})
r(1) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x7ddab8836da0>)
dr(2): (MsgType.NEIGHBORS: [1])
dr(2): (MsgType.GET_TOPOLOGY: None)
r(1) : (MsgType.NEIGHBORS: {'index': 2, 'neighbors': [1]})
r(2) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x7ddab8836ef0>)
r(0) : (MsgType.NEIGHBORS: {'index': 2, 'neighbors': [1]})
r(0) : (MsgType.PRINT_WAYS: None)
0: [[0], [0, 1], [0, 1, 2]]
r(2) : (MsgType.PRINT_WAYS: None)
2: [[2, 1, 0], [2, 1], [2]]
r(1) : (MsgType.PRINT_WAYS: None)
1: [[1, 0], [1], [1, 2]]
r(0) : (MsgType.PRINT_WAYS: None)
0: [[0], [0, 1], [0, 1, 2]]
r(1) : (MsgType.PRINT_WAYS: None)
1: [[1, 0], [1], [1, 2]]
r(2) : (MsgType.PRINT_WAYS: None)
2: [[2, 1, 0], [2, 1], [2]]
dr(0): (MsgType.OFF: None)
r(1) : (MsgType.OFF: 0)
r(2) : (MsgType.OFF: 0)
r(2) : (MsgType.PRINT_WAYS: None)
2: [[], [2, 1], [2]]
r(1) : (MsgType.PRINT_WAYS: None)
1: [[], [1], [1, 2]]
r(0) : (MsgType.PRINT_WAYS: None)
0: [[0], [], []]
dr(0): (MsgType.NEIGHBORS: [1])
dr(0): (MsgType.GET_TOPOLOGY: None)
r(0) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x7ddab88372b0>)
r(2) : (MsgType.NEIGHBORS: {'index': 0, 'neighbors': [1]})
r(0) : (MsgType.PRINT_WAYS: None)
0: [[0], [0, 1], [0, 1, 2]]
r(1) : (MsgType.NEIGHBORS: {'index': 0, 'neighbors': [1]})
r(1) : (MsgType.PRINT_WAYS: None)
1: [[], [1], [1, 2]]
r(2) : (MsgType.PRINT_WAYS: None)
2: [[], [2, 1], [2]]
dr(1): (MsgType.NEIGHBORS: [0])
dr(2): (MsgType.OFF: None)
r(1) : (MsgType.OFF: 2)
r(0) : (MsgType.NEIGHBORS: {'index': 1, 'neighbors': [0]})
r(0) : (MsgType.OFF: 2)
```

## Кольцевая топология
```
topology: circle

dr(0): (MsgType.NEIGHBORS: [2, 1])
dr(0): (MsgType.GET_TOPOLOGY: None)
dr(1): (MsgType.NEIGHBORS: [0, 2])
dr(1): (MsgType.GET_TOPOLOGY: None)
r(0) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x7ab13951ebf0>)
r(0) : (MsgType.NEIGHBORS: {'index': 1, 'neighbors': [0, 2]})
r(1) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x7ab13951ee90>)
dr(2): (MsgType.NEIGHBORS: [1, 0])
dr(2): (MsgType.GET_TOPOLOGY: None)
r(0) : (MsgType.NEIGHBORS: {'index': 2, 'neighbors': [1, 0]})
r(1) : (MsgType.NEIGHBORS: {'index': 2, 'neighbors': [1, 0]})
r(2) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x7ab13951ece0>)
r(2) : (MsgType.PRINT_WAYS: None)
2: [[2, 0], [2, 1], [2]]
r(0) : (MsgType.PRINT_WAYS: None)
0: [[0], [0, 1], [0, 2]]
r(1) : (MsgType.PRINT_WAYS: None)
1: [[1, 0], [1], [1, 2]]
r(0) : (MsgType.PRINT_WAYS: None)
0: [[0], [0, 1], [0, 2]]
r(1) : (MsgType.PRINT_WAYS: None)
1: [[1, 0], [1], [1, 2]]
r(2) : (MsgType.PRINT_WAYS: None)
2: [[2, 0], [2, 1], [2]]
dr(0): (MsgType.OFF: None)
r(2) : (MsgType.OFF: 0)
r(1) : (MsgType.OFF: 0)
r(1) : (MsgType.PRINT_WAYS: None)
1: [[], [1], [1, 2]]
r(2) : (MsgType.PRINT_WAYS: None)
2: [[], [2, 1], [2]]
r(1) : (MsgType.PRINT_WAYS: None)
1: [[], [1], [1, 2]]
r(2) : (MsgType.PRINT_WAYS: None)
2: [[], [2, 1], [2]]
r(0) : (MsgType.PRINT_WAYS: None)
0: [[0], [], []]
r(0) : (MsgType.PRINT_WAYS: None)
0: [[0], [], []]
dr(0): (MsgType.NEIGHBORS: [2, 1])
dr(0): (MsgType.GET_TOPOLOGY: None)
r(1) : (MsgType.NEIGHBORS: {'index': 0, 'neighbors': [2, 1]})
r(2) : (MsgType.NEIGHBORS: {'index': 0, 'neighbors': [2, 1]})
r(0) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x7ab13951ef20>)
dr(1): (MsgType.NEIGHBORS: [0])
dr(2): (MsgType.NEIGHBORS: [0])
r(1) : (MsgType.NEIGHBORS: {'index': 2, 'neighbors': [0]})
r(2) : (MsgType.NEIGHBORS: {'index': 1, 'neighbors': [0]})
r(0) : (MsgType.NEIGHBORS: {'index': 1, 'neighbors': [0]})
r(0) : (MsgType.NEIGHBORS: {'index': 2, 'neighbors': [0]})
dr(1): (MsgType.OFF: None)
r(2) : (MsgType.OFF: 1)
r(0) : (MsgType.OFF: 1)
```

## Звёздная топология
```
topology: star

dr(0): (MsgType.NEIGHBORS: [1])
dr(0): (MsgType.GET_TOPOLOGY: None)
r(0) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x76973b322e00>)
dr(1): (MsgType.NEIGHBORS: [0, 2, 3])
dr(1): (MsgType.GET_TOPOLOGY: None)
r(0) : (MsgType.NEIGHBORS: {'index': 1, 'neighbors': [0, 2, 3]})
dr(2): (MsgType.NEIGHBORS: [1])
dr(3): (MsgType.NEIGHBORS: [1])
dr(2): (MsgType.GET_TOPOLOGY: None)
dr(3): (MsgType.GET_TOPOLOGY: None)
r(3) : (MsgType.NEIGHBORS: {'index': 2, 'neighbors': [1]})
r(3) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x76973b3233d0>)
r(2) : (MsgType.NEIGHBORS: {'index': 3, 'neighbors': [1]})
r(2) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x76973b3233a0>)
r(1) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x76973b322fb0>)
r(1) : (MsgType.NEIGHBORS: {'index': 2, 'neighbors': [1]})
r(1) : (MsgType.NEIGHBORS: {'index': 3, 'neighbors': [1]})
r(0) : (MsgType.NEIGHBORS: {'index': 2, 'neighbors': [1]})
r(0) : (MsgType.NEIGHBORS: {'index': 3, 'neighbors': [1]})
r(3) : (MsgType.PRINT_WAYS: None)
3: [[3, 1, 0], [3, 1], [3, 1, 2], [3]]
r(0) : (MsgType.PRINT_WAYS: None)
0: [[0], [0, 1], [0, 1, 2], [0, 1, 3]]
r(1) : (MsgType.PRINT_WAYS: None)
1: [[1, 0], [1], [1, 2], [1, 3]]
r(2) : (MsgType.PRINT_WAYS: None)
2: [[2, 1, 0], [2, 1], [2], [2, 1, 3]]
r(2) : (MsgType.PRINT_WAYS: None)
2: [[2, 1, 0], [2, 1], [2], [2, 1, 3]]
r(3) : (MsgType.PRINT_WAYS: None)
3: [[3, 1, 0], [3, 1], [3, 1, 2], [3]]
r(0) : (MsgType.PRINT_WAYS: None)
0: [[0], [0, 1], [0, 1, 2], [0, 1, 3]]
r(1) : (MsgType.PRINT_WAYS: None)
1: [[1, 0], [1], [1, 2], [1, 3]]
dr(2): (MsgType.OFF: None)
r(3) : (MsgType.OFF: 2)
r(0) : (MsgType.OFF: 2)
r(1) : (MsgType.OFF: 2)
r(3) : (MsgType.PRINT_WAYS: None)
3: [[3, 1, 0], [3, 1], [], [3]]
r(0) : (MsgType.PRINT_WAYS: None)
0: [[0], [0, 1], [], [0, 1, 3]]
r(1) : (MsgType.PRINT_WAYS: None)
1: [[1, 0], [1], [], [1, 3]]
r(3) : (MsgType.PRINT_WAYS: None)
3: [[3, 1, 0], [3, 1], [], [3]]
r(1) : (MsgType.PRINT_WAYS: None)
1: [[1, 0], [1], [], [1, 3]]
r(0) : (MsgType.PRINT_WAYS: None)
0: [[0], [0, 1], [], [0, 1, 3]]
r(2) : (MsgType.PRINT_WAYS: None)
2: [[], [], [2], []]
r(2) : (MsgType.PRINT_WAYS: None)
2: [[], [], [2], []]
dr(2): (MsgType.NEIGHBORS: [1])
dr(2): (MsgType.GET_TOPOLOGY: None)
r(1) : (MsgType.NEIGHBORS: {'index': 2, 'neighbors': [1]})
dr(1): (MsgType.NEIGHBORS: [2])
r(0) : (MsgType.NEIGHBORS: {'index': 2, 'neighbors': [1]})
r(0) : (MsgType.NEIGHBORS: {'index': 1, 'neighbors': [2]})
r(2) : (MsgType.SET_TOPOLOGY: <topology.Topology object at 0x76973b322cb0>)
r(2) : (MsgType.NEIGHBORS: {'index': 1, 'neighbors': [2]})
dr(3): (MsgType.OFF: None)
r(1) : (MsgType.OFF: 3)
r(2) : (MsgType.OFF: 3)
r(0) : (MsgType.OFF: 3)
```
