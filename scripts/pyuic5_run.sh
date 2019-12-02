for entry in src/ui/*
do
  WOEXT="${entry%%.*}"
  EXT="${entry##*.}"
  if [ "$EXT" == "ui" ]; then
    pyuic5 "$entry" -o "$WOEXT".py
  fi
done
