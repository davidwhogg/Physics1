beginfig(1);

%Standardize on a 16u wide grid
u=0.357cm;

numeric axis_pen_weight;
numeric object_pen_weight;
numeric dot_pen_weight;

axis_pen_weight = 1;
object_pen_weight = 2;
dot_pen_weight = 4;

%Draw wall and floor
pickup pencircle scaled object_pen_weight;
draw (0u,4u)--(0u,0u)--(16u,0u);

%Draw wheel
pickup pencircle scaled object_pen_weight;
draw fullcircle scaled 4u shifted (12u,2u);

%Draw spring
pickup pencircle scaled object_pen_weight;
draw (0,2u)--(2u,2u);
for ix = 0 upto 5:
  draw (2u+ix*1u,2u){dir 45}..tension 1.5 and 1.5..(2.25u+ix*1u,3u)..tension 1.5 and 1.5..{dir -45}(2u+ix*1u,2u);
  draw (2u+ix*1u,2u){dir -45}..tension 1 and 1..{dir 45}(3u+ix*1u,2u);
endfor;
draw (8u,2u)--(12u,2u);

%Draw connector
pickup pencircle scaled dot_pen_weight;
draw (12u,2u);

%Label mass, spring, etc.
label.rt(btex $M$,$R$,$I$ etex, (14u,2u));
label.top(btex $k$ etex, (5u,3u));

endfig;
end;

