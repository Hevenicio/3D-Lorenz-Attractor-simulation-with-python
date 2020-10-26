# Atrator-de-Lorenz-em-Python
Plotagem animada do Atrator de Lorenz, implementada em Python usando o método de Runge-Kutta de 4ª ordem.

<div class="zoomable-image" style="display: block; margin-left: auto; margin-right: auto; width: 400px; height: 226px;"><img style="" src="https://user-images.githubusercontent.com/65929471/97085951-f61a7800-15f6-11eb-957b-18e9e0dfe326.gif" width="600"><a href="https://user-images.githubusercontent.com/65929471/97085951-f61a7800-15f6-11eb-957b-18e9e0dfe326.gif" class="zoomify-image"><span class="zoomify-text">Ampliar</span></a></div>

## Teoria
O atrator Lorenz é um conjunto de soluções caóticas de um sistema de equações diferenciais ordinárias chamado sistema de Lorenz. Estudado pela primeira vez por Edward Lorenz com a ajuda de Ellen Fetter, que desenvolveram um modelo matemático simplificado para a convecção atmosférica. O modelo é um sistema de três EDOs:

![xyz](https://wikimedia.org/api/rest_v1/media/math/render/svg/7928004d58943529a7be774575a62ca436a82a7f)

As variáveis de estado são x, y e z. A taxa na qual os estados estão mudando é denotada por dx/dt, dy/dt e dz/dt respectivamente. As constantes σ, ρ e β são os parâmetros físicos.
