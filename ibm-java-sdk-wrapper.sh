#!/bin/sh -p
#
# @(#)java_wrapper    99/03/09
#
# IBM Linux version
#
unset ENV

PRG="`/usr/bin/which $0`" >/dev/null 2>&1
progname="${0##*/}"
suffix="$(expr "$progname" : '.*\(_.$\)')"
JAVAHOME="${PRG%/*}/.."

# Resolve symlinks. See 4152645.
while [ -h "$PRG" ]; do
    ls="`/bin/ls -ld "$PRG"`"
    link="`/usr/bin/expr "$ls" : '.*-> \(.*\)$'`"
    if [ ! "$link" = "${link#/}" ]; then
        prg="$link"
    else
        prg="${PRG%/*}/$link"
    fi
    PRG="`/usr/bin/which $prg`" >/dev/null 2>&1
    JAVAHOME="${PRG%/*}/.."
done

# export JAVAHOME for GetPropertiesMD()
export JAVAHOME

JREHOME="$JAVAHOME/jre"

# Where is the JRE in relation to the executable?
unset jre
if [ -f "${JREHOME}/bin/libjava${suffix}.so" ]; then
    jre="${JREHOME}"
fi
if [ -f "${JAVAHOME}/bin/libjava${suffix}.so" ]; then
    jre="${JAVAHOME}"
fi
if [ "x${jre}" = "x" ]; then
    echo "Error: can't find libjava${suffix}.so"
    exit 1
fi

LD_LIBRARY_PATH="$jre/bin:$jre/bin/classic:$LD_LIBRARY_PATH"
export LD_LIBRARY_PATH

prog="$JAVAHOME/bin/exe/${progname}"

# Run.
if [ -x "$prog" ]
then
    exec $DEBUG_PROG "$prog" "$@"
else
    echo >&2 "$progname was not found in $JAVAHOME/bin/exe"
    exit 1
fi
