# [level 0] 홀짝에 따라 다른 값 반환하기 - 181935 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181935?language=python3) 

### 성능 요약

메모리: 9.14 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 11월 03일 14:51:41

### 문제 설명

<p>양의 정수 <code>n</code>이 매개변수로 주어질 때, <code>n</code>이 홀수라면 <code>n</code> 이하의 홀수인 모든 양의 정수의 합을 return 하고 <code>n</code>이 짝수라면 <code>n</code> 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>7</td>
<td>16</td>
</tr>
<tr>
<td>10</td>
<td>220</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>n</code>은 7로 홀수입니다. 7 이하의 모든 양의 홀수는 1, 3, 5, 7이고 이들의 합인 1 + 3 + 5 + 7 = 16을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

1. 우선 문제를 읽는다
2. 주석으로 내가 이 문제를 이해한 바를 적는다.
    1. n이 홀수인지 짝수인지 판단 후에 홀수라면 n 이하의 홀수들을 모두 더해 반환. 짝수라면 n 이하의 짝수인 모든 양의 정수 제곱을 모두 더해 반환.
3. 문제의 본질을 파악해 적는다.
    1. 우선 n이 홀수인지 짝수인지 % 연산을 통해 파악할 수 있어야 한다.
    2. 양의 정수부터 n 까지 반복문을 돌면서 홀짝판단을 해서 값을 계속 더해 나가야 한다.
    3. 홀수인 경우엔 덧셈연산으로 짝수인 경우엔 제곱연산을 추가해서 덧셈연산으로
4. 무엇을 활용하여 해결할지 파악해 적는다.
    1. 홀짝 판단을 위해서 % 연산과 if 문을 활용한다.
    2. 양의 정수 1부터 n까지 홀or짝을 더하기 위해 `for i in range (1,n+1)` 반복문을 활용한다.
    3. 짝수의 경우엔 제곱연산을 위해서 `**` 연산을 활용한다.
    4. 반환할 변수에 += 연산을 활용해 값을 계속 더해 나간다.
5. 그것을 활용하는 데 필요한 자료구조를 파악해 적는다.
    1. 따로 활용할 자료구조는 없고 리턴할 변수에 값을 계속 더해 나간다.

- 시간 복잡도 분석
    - 입력의 길이는? : 1 ≤ `n` ≤ 100
    - 시간 복잡도는? :

- 테스트 실행

- 첫번째 코드
    
    ```python
    def solution(n):
        result = 0
        if((n%2) == 0):
            for i in range(1,n+1):
                if (i%2 == 0):
                    result += (i^2)
        else:
            for i in range(1,n+1):
                if (i%2 != 0):
                    result += i
        return result
            
    ```
    
    틀린이유 : 제곱 연산의 연산기호를 잘못알고 있었다. 제곱 연산은 `**`을 활용한다.
    
- 두번째 코드
    
    ```python
    def solution(n):
        result = 0
        if((n%2) == 0):
            for i in range(1,n+1):
                if (i%2 == 0):
                    result += (i**2)
        else:
            for i in range(1,n+1):
                if (i%2 != 0):
                    result += i
        return result
            
    ```

<ul>
<li>예제 2번의 <code>n</code>은 10으로 짝수입니다. 10 이하의 모든 양의 짝수는 2, 4, 6, 8, 10이고 이들의 제곱의 합인 2<sup>2</sup> + 4<sup>2</sup> + 6<sup>2</sup> + 8<sup>2</sup> + 10<sup>2</sup> = 4 + 16 + 36 + 64 + 100 = 220을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
