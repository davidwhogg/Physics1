all:
	(cd mp ; make)
	(cd pro ; make)
	(cd tex ; make)

clean:
	(cd tex ; make clean)
	(cd pro ; make clean)
	(cd mp ; make clean)
