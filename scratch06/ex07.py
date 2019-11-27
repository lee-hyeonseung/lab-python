"""
중심 극한 정리(Central Limit Theorem):
모집단이 어떤 분포든지 상관없이, 표본의 크기가 충분이 크다면
모든 가능한 표본 평균은 모평균 주위에서 정규분포를 따른다.
만약 모집단이 평균이 mu이고, 표준편차가  sigma인 정규 분포를 따른다면,
표본 평균의 분포는 평균이 mu이고, 분산이 sigma/sqrt(n)인 정규분포를 띤다.

베르누이 확률 변수(Bernoulli random variable):
    어떤 시행의 결과가 '성공', '실패' 중 하나로 나타나고,
    성공의 확률이 p, 실패할 확률이 1-p라고 할 때
    그 결과가 성공이면 확률 변수는 1을 갖고,
    결과가 실패면 확률 변수는 0을 갖는 확률 변수 x

베르누이 확률 질량 함수(PMF: Probability Mass Function)
    pmf(x) = p if x = 1, 0 if x = 0
           = (p ** x)((1-p)**(1-x))

이항 확률 변수 (binominal random variable):
    n개의 독립적인 베르누이 확률 변수들을 더한 것

(비유)
베르누이 확률 변수 -> 동전 한 개를 던질 때 앞면의 수
이항 확률 변수 -> 동전 N개를 던질 때 앞면의 수

베르누이 확률 변수의 기댓값(평균) = p, 표준 편차 = sqrt(p(1-p))
중심 극한 정리: n이 적당히 크다면, 이항 확률 변수는 대략
평균이 np이고, 표준 편차가 sqrt(np(q-p))인
정규 분포의 확률 변수와 같다.
-> 표본(sample)의 평균(np)와 분산(np(1-p))을 알아내면,
    모집단(population)의 평균(p)와 분산(p(1-p))를 예측할 수 있다.
"""
import math
import random
from collections import Counter
import matplotlib.pyplot as plt

from scratch06.ex06 import normal_cdf


def bernoulli_trial(p):
    """베르누이 확률 변수 1 또는 0을 확률 p에 따라서 return"""
    x = random.random()  # random(): 0이상 1미만의 난수를 return
    return 1 if x < p else 0


def binominal(n, p):
    """1이 나올 확률이 p인 베르누이 실행을 n번 했을 때,
    1이 나오는 회수를 return. 이항 확률 변수를 return"""
    s = 0  # 1이 나오는 횟수
    for _ in range(n):
        s += bernoulli_trial(p)
    return s


if __name__ == '__main__':
    trials = 10_000
    n = 100  # 동전을 전지는 횟수
    p = 0.5  # 동전을 던졌을 때 앞 면이 나올 확률
    data = [binominal(n, p) for _ in range(trials)]
    # plt.hist(data)
    # plt.show()
    # 이항 확률 변수와 그에 따른 확률값을 그리기 위해서
    histogram = Counter(data)
    x_bar = [k for k in histogram.keys()]
    y_bar = [v / trials for v in histogram.values()]
    plt.bar(x_bar, y_bar, color='0.75')

    # 이항 확률 변수의 정규 분포 근사(approximation)
    # 이항 확률 변수의 분포는 n이 충분히 크면 정규 분포가 된다.
    mu = n * p  # 평균
    sigma = math.sqrt(n * p * (1 - p))  # 표준편차
    # 정규 분포 그래프를 그리기 위해서
    x_line = range(min(data), max(data) + 1)  # range(0, n+1)
    y_line = [normal_cdf(x + 0.5, mu, sigma) - normal_cdf(x - 0.5, mu, sigma)
              for x in x_line]
    plt.plot(x_line, y_line)
    plt.show()
