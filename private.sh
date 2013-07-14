TMP=$(mktemp)
#rmdir $TMP
git clone https://github.com/ahdinosaur/cloyne-network-private.git $TMP
cp -R cloyne-network-private/* .
