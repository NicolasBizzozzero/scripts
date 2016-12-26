#rm -Rf ~/
if [ -d ~/".cache" ]; then
        rm -Rf ~/".cache"
fi

if [ -f ~/".python_history" ]; then
        rm ~/".python_history"
fi

if [ -f ~/".bash_history" ]; then
        rm ~/".bash_history"
fi

if [ -d ~/".gradle" ]; then
        rm -Rf ~/".gradle"
fi

if [ -d ~/".local" ]; then
        rm -Rf ~/".local"
fi

if [ -d ~/".netbeans" ]; then
        rm -Rf ~/".netbeans"
fi

if [ -d ~/".java" ]; then
        rm -Rf ~/".java"
fi

exit 0
