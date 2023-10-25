hdir=$(pwd)
for zipped in $(ls *_ASSIGN6_CPSC110.zip); do
    echo '----------------------------------------'
    echo 'testing' $zipped
    unzip $zipped
    cd $(basename -s .zip $zipped)
    for fname in test_max.py test_rewrite.py test_DNA.py; do
        cp ../$fname .
        python $fname
    done
    cd $hdir
done