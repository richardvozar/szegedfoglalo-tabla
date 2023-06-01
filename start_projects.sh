echo "****************************"
echo "* Starting all projects... *"
echo "****************************"

echo "--Starting felhasznalo project--"
nohup python3 /szegedfoglalo/szegedfoglalo_felhasznalo/main.py &
echo "--Felhasznalo project started--"
sleep 3

echo "--Starting lobby project--"
nohup python3 /szegedfoglalo/szegedfoglalo_lobby/main.py &
echo "--Lobby project started--"
sleep 3

#echo "--Starting kvizk project--"
#nohup python3 /szegedfoglalo/kviz/app.py &
#echo "--Lobby project started--"
#sleep 3


echo "--Starting tabla project--"
nohup python3 /szegedfoglalo/szegedfoglalo_tabla/app.py &
echo "--Tabla project started--"
sleep 3


echo "--Starting kiertekeles project--"
nohup python3 /szegedfoglalo/szegedfoglalo_kiertekeles/kiertekeles/app.py &
echo "--Kiertekeles project started--"
sleep 3

echo "***************************************"
echo "* Szegedfoglalo projects are running! *"
echo "***************************************"