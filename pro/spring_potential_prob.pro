pro spring_potential_prob

; define position vector (m)
  x= -10d0+0.01*dindgen(2000)

; define potential function
  U0= -1.0d0                 ; (J)
  x0= -2.0d0                 ; (m)
  keff= 4.0d0                ; (N/m)
  U= U0+0.5d0*keff*(x-x0)^2  ; (J)

; setup postscript plot
  !P.FONT= -1 & !P.BACKGROUND= 255 & !P.COLOR= 0
  set_plot, "PS"
  xsize= 5.0 & ysize= 3.0
  device, file='spring_potential_prob.eps',/inches,xsize=xsize,ysize=ysize, $
    xoffset=(8.5-xsize)/2.0,yoffset=(11.0-ysize)/2.0,/color,bits_per_pixel=24
  !P.THICK= 4.0
  !P.CHARTHICK= !P.THICK & !X.THICK= !P.THICK & !Y.THICK= !P.THICK
  !P.CHARSIZE= 1.2
  !X.CHARSIZE= !P.CHARSIZE & !Y.CHARSIZE= !P.CHARSIZE
  !P.PSYM= 0
  !P.TITLE= ''
  !X.STYLE= 1
  !X.TITLE= ''
  !X.RANGE= [-3.0,3.0]+x0
  !X.MARGIN= [6,0]
  !X.OMARGIN= [1,1]
  !X.TICKLEN= 1.0
  !Y.STYLE= 1
  !Y.TITLE= ''
  !Y.RANGE= [-2.0,8.0]
  !Y.MARGIN= 0.6*!X.MARGIN
  !Y.OMARGIN= 0.6*!X.OMARGIN
  !Y.TICKLEN= 1.0
  !P.MULTI= 0
  xyouts, 0,0,'!3'

; plot
  djs_plot, x,U,thick=16,xtitle='!8x!3  (m)',ytitle='!8U!3  (J)'

; close
  device,/close
  return
end
