./RunPRPForCurDomain.sh llvisitall
./PrintHuman_Policy.sh llvisitall
python ./DrawDotPolicy.py -domainname llvisitall

./RunPRPForCurDomain.sh reversell
./PrintHuman_Policy.sh reversell
python ./DrawDotPolicy.py -domainname reversell

./RunPRPForCurDomain.sh blocks_clear
./PrintHuman_Policy.sh blocks_clear
python ./DrawDotPolicy.py -domainname blocks_clear

./RunPRPForCurDomain.sh stripedtower
./PrintHuman_Policy.sh stripedtower
python ./DrawDotPolicy.py -domainname stripedtower

./RunPRPForCurDomain.sh treetraversal
./PrintHuman_Policy.sh treetraversal
python ./DrawDotPolicy.py -domainname treetraversal

./RunPRPForCurDomain.sh RGBBlocks
./PrintHuman_Policy.sh RGBBlocks
python ./DrawDotPolicy.py -domainname RGBBlocks

