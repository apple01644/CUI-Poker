# CUI-Poker
python으로 만든 포커 프로그램입니다.
CUI로 조작이 가능하며 1, 2, 3, 4만 입력 할 수 있으면
플레이가 가능합니다.

[Pydroid 3](play.google.com/store/apps/details?id=ru.iiec.pydroid3)를 설치 하시면
안드로이드에서도 플레이 가능합니다!

# 실제 게임 진행 과정
```
---===---give four cards---===---
!you get ♣T
!you get ♥9
!you get ♣7
!you get ◆2
---===---throw one hiden card---===---
your hand [♣T, ♥9, ♣7, ◆2]
throw one card>1
---===---show the card---===---
your hand [♥9, ♣7, ◆2]
show one card>2
Queen    's shown
>◆8
Bishorp  's shown
>♠4
Rock     's shown
>♠5
King     's shown
>♥A
Pone     's shown
>♠2
---===---round table---===---
['Call', 'Die'] Your chips 16 ,Now deal 1
[♥9, ♣7, ◆2]
select>1
ⓒall 1
Queen
ⓒall 1
Bishorp
ⓒall 1
Rock
ⓒall 1
King
ⓒall 1
Pone
ⓒall 1
---===---give one cards---===---
Pone      [♠2, ◆A]
King      [♥A, ♥3]
Rock      [♠5, ♥T]
Queen     [◆8, ♣9]
Bishorp   [♠4, ◆6]
!you get ♥2
---===---round table---===---
Pone
ⓡaise to 1
King
ⓒall 1
Rock
ⓒall 1
Queen
ⓒall 1
Bishorp
ⓒall 1
['Call', 'Die', 'Raise'] Your chips 15 ,Now deal 1
[♥9, ♣7, ◆2, ♥2]
select>2
ⓓie
---===---give two cards---===---
King      [♥A, ♥3, ♠7]
Bishorp   [♠4, ◆6, ♥4]
Queen     [◆8, ♣9, ♠8]
Pone      [♠2, ◆A, ♣3]
Rock      [♠5, ♥T, ◆K]
------------------
King      [♥A, ♥3, ♠7, ♣2]
Bishorp   [♠4, ◆6, ♥4, ♠3]
Queen     [◆8, ♣9, ♠8, ♠9]
Pone      [♠2, ◆A, ♣3, ◆T]
Rock      [♠5, ♥T, ◆K, ◆7]
---===---round table---===---
King
ⓒheck
Bishorp
ⓒheck
Queen
ⓒheck
Pone
ⓒheck
Rock
ⓡaise to 1
King
ⓡaise to 3
Bishorp
ⓒall 3
Queen
ⓒall 3
Pone
ⓓie
Rock
ⓒall 3
---===---give one cards---===---
---===---round table---===---
Queen
ⓒheck
King
ⓡaise to 1
Bishorp
ⓒall 1
Rock
ⓒall 1
Queen
ⓒall 1
---===---throw two cards---===---
---===---final act---===---
King      [♥A, ♥3, ♠7, ♣2, ♣4] Top 6
Knight    [♥9, ♣7, ◆2, ♥2] died you 15
Rock      [♥K, ♥Q, ♠5, ♥T, ◆K] A pair 24
Queen     [♥J, ♠T, ♣9, ♠8, ♣8] A pair 22
Bishorp   [◆4, ♠4, ♥4, ♠3, ◆9] Triple ☆ 8 + 27
Pone      [♥6, ◆3, ♠2, ◆A, ♣3, ◆T] died 19
---===---end---===---
```
