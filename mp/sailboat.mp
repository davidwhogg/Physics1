% sailboat, sail and wind
% 2001-Oct-26  written by Hogg

beginfig(1) ;
  u=0.6cm ;

% define angles
  numeric boat_angle ;
  boat_angle= 90 ;
  numeric sail_angle ;
  sail_angle= 50 ;

% define pen weights
  numeric axis_pen_weight ;
  numeric curve_pen_weight ;
  numeric joint_pen_weight ;
  numeric vector_pen_weight ;
  axis_pen_weight=     0.5 ;
  curve_pen_weight=    1.0 ;
  vector_pen_weight=   2.0 ;
  joint_pen_weight=    4.0 ;

% draw axes
  pickup pencircle scaled axis_pen_weight ;
  path p[] ;
  p1= (1,0)--(-1,0) ;
  p2= p1 scaled -4.0u rotated 90 ;
  p3= p1 scaled -4.0u rotated (boat_angle-90) ;
  p4= p1 scaled 4.0u rotated (boat_angle-sail_angle) ;
  draw p2 ;
  draw p3 ;
  draw p4 ;

% mark angles
  pickup pencircle scaled axis_pen_weight ;
  p5= fullcircle rotated (80) scaled 4u cutbefore p3 cutafter p2 ;
  p6= fullcircle scaled -6u cutbefore p2 cutafter p4 ;
  p7= ((0,1)--(1,1)--(1,0)) scaled 0.3u rotated (boat_angle-sail_angle-90) ;
  z5= point 0.5*length(p5) of p5 ;
  z6= point 0.5*length(p6) of p6 ;
  draw p5 ;
  draw p6 ;
  draw p7 ;
  label.llft(btex $\beta$ etex, z5) ;
  label.rt(btex $\theta$ etex, z6) ;

% define path for hull
  path hull ;
  hull= (0,1){dir -45}..(1,-0.5)..tension 1.2..(0.5,-2.5)--(-0.5,-2.5)..tension 1.2..(-1,-0.5)..{dir 45}cycle ;

% define path for sail
  path sail ;
  sail= (0,0)--(0,-2) ;

% draw hull and sail
  pickup pencircle scaled curve_pen_weight ;
  draw hull scaled u rotated boat_angle ;
  draw sail scaled u rotated (boat_angle-sail_angle) ;
  pickup pencircle scaled joint_pen_weight ;
  draw (0,0) ;

% draw vectors
  path v[] ;
  v1= (0,0)--(1,0) ;
  v2= v1 scaled 2u rotated -90 shifted (0,4u) ;
  v3= v1 scaled u shifted (0,-u) rotated (boat_angle-sail_angle) ;
  v4= v1 scaled 2u shifted (1.2u,0) rotated (boat_angle+90) ;
  z2= point 0.5*length(v2) of v2 ;
  z3= point 0.7*length(v3) of v3 ;
  z4= point 0.5*length(v4) of v4 ;
  pickup pencircle scaled vector_pen_weight ;
  drawarrow v2 ;
  drawarrow v3 ;
  drawarrow v4 ;
  label.rt(btex $\vec{p}_i$ etex, z2) ;
  label.lrt(btex $\hat{n}$ etex, z3) ;
  label.urt(btex $\vec{v}$ etex, z4) ;

endfig ;
end
