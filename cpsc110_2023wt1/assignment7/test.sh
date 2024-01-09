hdir=$(pwd)
for zipped in $(ls *_ASSIGN7_CPSC110.zip); do
    echo '----------------------------------------'
    echo 'testing' $zipped
    unzip $zipped -d $(basename -s .zip $zipped)
    cd $(basename -s .zip $zipped)
    for fname in test_add.py; do
        cp ../$fname .
        python $fname
    done
    cd $hdir
done
