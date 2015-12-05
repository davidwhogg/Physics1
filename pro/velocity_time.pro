pro velocity_time

; define velocity and time vectors
  t= [ 0d, 50,100,150,200,250,300,350, 400,450, 500]
  v= [10d, 15, 20, 20, 10,  0,-10,-7.5, -5,-2.5,  0]

; setup postscript plot
  !P.FONT= -1 & !P.BACKGROUND= 255 & !P.COLOR= 0
  set_plot, "PS"
  xsize= 7.5 & ysize= 3.5
  device, file='velocity_time.eps',/inches,xsize=xsize,ysize=ysize, $
    xoffset=(8.5-xsize)/2.0,yoffset=(11.0-ysize)/2.0,/color,bits_per_pixel=24
  !P.THICK= 4.0
  !P.CHARTHICK= !P.THICK & !X.THICK= !P.THICK & !Y.THICK= !P.THICK
  !P.CHARSIZE= 1.2
  !X.CHARSIZE= !P.CHARSIZE & !Y.CHARSIZE= !P.CHARSIZE
  !P.PSYM= 0
  !P.TITLE= ''
  !X.STYLE= 1
  !X.TITLE= ''
  !X.RANGE= 0
  !X.MARGIN= [6,0]
  !X.OMARGIN= [3,1.5]
  !X.TICKLEN= 1.0
  !Y.STYLE= 3
  !Y.TITLE= ''
  !Y.RANGE= 0
  !Y.MARGIN= [2.5,0]
  !Y.OMARGIN= 0.5*!X.OMARGIN
  !Y.TICKLEN= 1.0
  !P.MULTI= 0
  xyouts, 0,0,'!3'

; plot
  djs_plot, t,v,thick=8,xtitle='time  !8t!3  (s)', $
    ytitle='!8x!3-velocity  !8v_x!3  (ms^{-1})'

  device,/close
  return
end
