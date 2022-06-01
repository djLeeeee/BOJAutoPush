# [Diamond III] Algorithm Teaching - 18029 

[문제 링크](https://www.acmicpc.net/problem/18029) 

### 성능 요약

메모리: 127300 KB, 시간: 2536 ms

### 분류

이분 매칭(bipartite_matching)

### 문제 설명

<p>The Latin American Beginners Regional Contest is coming, and the University of Byteland wants to prepare a team of newly-admitted students to compete. The university has N teachers that can instruct students in the topic of algorithms. Each candidate student must be trained by a single teacher, in a non-empty subset of the algorithms that the teacher knows. For example, if a given teacher knows the two algorithms PRIM and KRUSKAL, then the teacher can train a student just on PRIM, just on KRUSKAL, or on both PRIM and KRUSKAL. As you can see, in this case there are three different options for this particular teacher to train a student. In general, a given teacher that knows A different algorithms can train a student in 2<sup>A</sup> − 1 different ways. All these 2<sup>A</sup> − 1 options can be carried out, because the university has a lot of new students, and there is no limit on the number of students a teacher can train.</p>

<p>The university would like to form a team having as many students as possible. However, each pair of students in the final team must be able to cooperate, which means that each one of them must have been trained on an algorithm that the other hasn’t. For example, a student trained on BFS and DFS can cooperate with another student trained on DFS and DIJKSTRA, because the first student is trained on BFS while the second student isn’t, and the second student is trained on DIJKSTRA while the first student isn’t. On the other hand, a student trained on BFS and DFS cannot cooperate with another student trained just on BFS, or just on DFS, or on both BFS and DFS, among others.</p>

<p>Given the set of algorithms that each teacher knows, you must determine the maximum number of students in a team in which every student can cooperate with each other. Recall that each student must be trained by a single teacher, while each teacher can train as many students as needed. For example, if there is just one teacher who knows the algorithms DFS, BFS and DIJKSTRA, it is possible to prepare a team with up to three students: a first student trained on DFS and BFS, a second student trained on DFS and DIJKSTRA, and a third student trained on BFS and DIJKSTRA.</p>

### 입력 

 <p>The first line contains an integer N (1 ≤ N ≤ 100) indicating the number of teachers. Each of the next N lines describes a teacher with an integer A (1 ≤ A ≤ 10) representing the number of algorithms the teacher knows, followed by A different non-empty strings of at most 10 uppercase letters each, indicating the names of the algorithms that teacher knows.</p>

### 출력 

 <p>Output a single line with an integer indicating the maximum number of students in a team in which every student can cooperate with each other.</p>

