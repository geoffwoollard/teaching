hdir=$(pwd)
for zipped in $(ls *_ASSIGN9_CPSC110.zip); do
    echo '----------------------------------------'
    echo 'testing' $zipped
    unzip $zipped -d $(basename -s .zip $zipped)
    cd $(basename -s .zip $zipped)
    for fname in test_*.py; do
        cp ../$fname .
        python $fname
    done
    cd $hdir
done
