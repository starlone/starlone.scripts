PARAM=$1;
STRING1=$2;
STRING2=$3;
corrige() {
    FROM=$1
    TO=$2

    echo 'procurando arquivos'

    ARQUIVOS=`grep -RIi $FROM . | cut -f1 -d: | uniq | grep -v replacestrings.sh | grep -v '\.hg' | grep -v '\.svn'`
    echo alterando arquivos
    for arquivo in $ARQUIVOS
    do
       printf '.'
       sed 's#'$FROM'#'$TO'#g;' -i $arquivo

    done
    echo 'OK'
}

case $PARAM in

    'replace')
        FROM=$STRING1
        TO=$STRING2
        corrige $FROM $TO
    ;;

    *)
        echo "Não existe esta opção!\n"
    ;;
esac


