pfile=$1

cp $1 $1.bak


sed -i -e 's/ , /, /g' $1
sed -i -e 's/ : /: /g' $1
sed -i -e 's/ ; /; /g' $1
sed -i -e 's/ - /-/g' $1
sed -i -e 's/ \x27 /\x27/g' $1

sed -i -e 's/\ ?\ /?  /g' $1
sed -i -e 's/\ !\ /!  /g' $1
sed -i 's/\ \.\ /\.  /g' $1
# sed -i 's/\ \x2E/\.  /g' $1

# Capitalize the first letter of every line
sed -i 's/[[:alpha:]]/\u&/' $1

nep=`grep ENDPOEM $1 | wc -l`
nep=`expr ${nep} - 1`

csplit $1 /ENDPOEM/ {$nep}

rm *.edt
rm ${pfile}.cap

for f in xx*
do
	cat $f | grep -v ENDPOEM > ${f}.edt
#	sed -i -e '1 s/.*/\U&/g;' ${f}.edt
	sed -i -e '1 s/^./\U&/g; 1 s/ ./\U&/g' ${f}.edt
	echo -e "ENDPOEM" >> ${f}.edt
	cat ${f}.edt >> ${pfile}.cap
done

sed -i -e 's/ i\x27/ I\x27/g' ${pfile}.cap
sed -i -e 's/ i\x2C/ I\x2C/g' ${pfile}.cap

sed -i -e 's/ i\./ I\./g' ${pfile}.cap

sed -i -e 's/ i\x3B/ I\x3B/g' ${pfile}.cap
sed -i -e 's/ i\x3A/ I\x3A/g' ${pfile}.cap
sed -i -e 's/ i\x3F/ I\x3F/g' ${pfile}.cap
sed -i -e 's/ i\x33/ I\x33/g' ${pfile}.cap
sed -i -e 's/ i / I /g' ${pfile}.cap

rm xx*
rm *.edt
