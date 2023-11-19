hdir=$(pwd)
for zipped in $(ls *_ASSIGN8_CPSC110.zip); do
    echo '----------------------------------------'
    echo 'testing' $zipped
    unzip $zipped -d $(basename -s .zip $zipped)
    cd $(basename -s .zip $zipped)
    for fname in test_library.py; do
        cp ../$fname .
        python $fname
    done
    cd $hdir
done
