# Atrator-de-Lorenz-em-Python
Plotagem animada do Atrator de Lorenz, implementada em Python usando o método de Runge-Kutta de 4ª ordem.

![Lorenz](https://user-images.githubusercontent.com/65929471/97719774-3f127680-1aa6-11eb-9b83-0535a56469f5.gif)

## Teoria
O atrator Lorenz é um conjunto de soluções caóticas de um sistema de equações diferenciais ordinárias chamado sistema de Lorenz. Estudado pela primeira vez por Edward Lorenz com a ajuda de Ellen Fetter, que desenvolveram um modelo matemático simplificado para a convecção atmosférica. O modelo é um sistema de três EDOs:

![xyz](https://wikimedia.org/api/rest_v1/media/math/render/svg/7928004d58943529a7be774575a62ca436a82a7f) <img src="https://static.wixstatic.com/media/5769f0_a8eef2121b814552a4f94b2796cc6d5b~mv2.gif"  width="110">

As variáveis de estado são x, y e z. A taxa na qual os estados estão mudando é denotada por dx/dt, dy/dt e dz/dt respectivamente. As constantes σ, ρ e β são os parâmetros físicos.

