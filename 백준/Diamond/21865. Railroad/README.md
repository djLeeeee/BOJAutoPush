# [Diamond IV] Railroad - 21865 

[문제 링크](https://www.acmicpc.net/problem/21865) 

### 성능 요약

메모리: 226680 KB, 시간: 3044 ms

### 분류

2-sat(2_sat), 그래프 이론(graphs), 강한 연결 요소(scc)

### 문제 설명

<p>평소 "더 지니어스"라는 프로그램을 좋아하던 태수는 데스매치에서 나왔던 모노레일 게임에 관심을 갖기 시작했고 더 다양한 종류의 타일을 이용한 게임을 하나 만들어왔다.</p>

<p>기존 모노레일 게임은 다음과 같은 2개의 타일만을 이용해서 플레이가 진행됐다. (각각 1번 타일(좌), 2번 타일(우)이라 칭한다.)</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/28f827ea-5c7a-4b26-97fc-beb899f9aaed/-/preview/" style="zoom:80%;"></p>

<p>하지만 태수는 여기에 다음과 같은 2종류의 타일을 추가하려고 한다. (각각 3번 타일(좌), 4번 타일(우)이라 칭한다.)</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/148d936c-6121-40c0-91f8-38dc088e0b99/-/preview/" style="zoom:75%;"></p>

<p>우리는 이 타일들이 무한히 많이 있는 상태로 게임을 진행한다. 원래의 모노레일 게임은 두 명의 플레이어가 서로 번갈아가며 타일을 놓지만, 친구가 없는 태수는 이러한 게임을 할 수 없기 때문에 살짝 다른 스타일로 게임을 진행하려고 한다.</p>

<blockquote>
<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>×</mo><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N \times M$</span></mjx-container> 크기의 격자가 있다. 각 타일을 놓을 수 있는 곳은 정해져있다. 격자에서 <code>L</code>이 써있는 곳은 1번 타일을 놓아야만 하고, <code>O</code>가 써있는 곳은 3번 또는 4번 타일을 놓아야만 한다. <code>X</code>가 써있는 곳은 어느 타일도 놓을 수 없고, <code>.</code>이 써있는 곳은 2번 타일을 놓거나 아예 놓지 않아야한다. 타일을 회전시켜 격자에 놓아도 된다고 할 때, 중간에 초록색 길이 끊겨있는 부분 없이 전부 이어지도록 타일을 놓으려고 한다. 과연 어떻게 놓아야하겠는가?</p>
</blockquote>

<p>태수가 이 게임을 성공할 수 있을지 판단하고, 가능하다면 그러한 배치를 찾아주는 프로그램을 작성하자.</p>

### 입력 

 <p>첫째 줄에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 공백을 사이에 두고 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>,</mo><mi>M</mi><mo>≤</mo><mn>300</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \leq N,M \leq 300)$</span></mjx-container> 그 다음 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>줄에 걸쳐 <code>L</code>, <code>O</code>, <code>X</code>, <code>.</code>으로만 이루어진 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>의 문자열이 주어진다.</p>

### 출력 

 <p>조건에 맞는 배치를 만들 수 없다면 첫째 줄에 <code>NO</code>를 출력한다. 그렇지 않다면 첫째 줄에 <code>YES</code>를 출력하고, 두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>줄에 걸쳐 해당 배치를 출력한다.</p>

<p>입력에서 <code>X</code>로 주어진 부분은 출력에서도 <code>X</code>로 출력해야하고, 빈공간은 <code>.</code>, 나머지는 아래 그림에 맞춰 출력하면 된다. (괄호 안은 아스키 코드 값을 의미한다. 예제에서 모든 타일에 대한 정보가 주어지니 정확히 무엇인지 모르겠으면 복사 붙여넣기를 활용하도록 하자.)</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/a221503c-1e7d-42d6-b13f-92806ee501fa/-/preview/" style="zoom:50%;"><br>
<img alt="" src="https://upload.acmicpc.net/274de2fe-cc68-47bf-aac9-85a125bd97f7/-/preview/" style="zoom:50%;"></p>

