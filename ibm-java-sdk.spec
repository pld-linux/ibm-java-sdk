
%define java	IBMJava2-13

%define __spec_install_post exit 0

Summary:	IBM Java Software Developement Kit v1.3
Name:		ibm-java-sdk
Version:	1.3
Release:	1
License:	Look into documentation
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source0:	IBMJava2-SDK-13.tgz
Source1:	ibm-java-sdk-wrapper.sh
URL:		http://www.ibm.com/developer/java
Provides:	java1.3
ExclusiveArch:	%{ix86}
BuildRequires:	file
Requires:	/usr/bin/which
Requires:	/bin/ls
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is IBM's Java 1.3 SDK.

%description -l pl
Pakiet zawiera SDK Javy 1.3 firmy IBM.

%prep
%setup -q -n %{java}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/%{java}/{bin,jre/bin/classic} \
	$RPM_BUILD_ROOT%{_prefix}/X11R6/lib/netscape/plugins \
	$RPM_BUILD_ROOT%{_includedir}/jdk \
	$RPM_BUILD_ROOT%{_bindir}

cp -a bin/exe $RPM_BUILD_ROOT%{_libdir}/%{java}/bin/
cp -a jre/bin/exe $RPM_BUILD_ROOT%{_libdir}/%{java}/jre/bin/
cp -a lib $RPM_BUILD_ROOT%{_libdir}/%{java}/
cp -a jre/lib $RPM_BUILD_ROOT%{_libdir}/%{java}/jre/

install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/%{java}/bin/jwrapper
for i in bin/*; do
	file $i | grep -q "shell" && \
	ln $RPM_BUILD_ROOT%{_libdir}/%{java}/bin/jwrapper \
		$RPM_BUILD_ROOT%{_libdir}/%{java}/$i
	ln -sf %{_libdir}/%{java}/$i \
		$RPM_BUILD_ROOT%{_bindir}/"$( basename "$i" )"
done
for i in jre/bin/*; do
	file $i | grep -q "shell" && \
	ln $RPM_BUILD_ROOT%{_libdir}/%{java}/bin/jwrapper \
		$RPM_BUILD_ROOT%{_libdir}/%{java}/$i
done

install jre/bin/*.so $RPM_BUILD_ROOT%{_libdir}/%{java}/jre/bin
install jre/bin/javaplugin.so $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/netscape/plugins
install jre/bin/java_vm* $RPM_BUILD_ROOT%{_libdir}/%{java}/jre/bin
install jre/bin/jvmtcf* $RPM_BUILD_ROOT%{_libdir}/%{java}/jre/bin
install include/* $RPM_BUILD_ROOT%{_includedir}/jdk
install jre/bin/classic/*.so $RPM_BUILD_ROOT%{_libdir}/%{java}/jre/bin/classic/

gzip -9nf docs/COPYRIGHT jre/bin/classic/Xusage.txt \
	jre/lib/jvm.hprof.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* javasrc.jar jre/bin/classic/Xusage.txt.gz
%doc jre/lib/jvm.hprof.txt.gz

%{_includedir}/jdk/*.h

%{_libdir}/%{java}/lib/*
%{_libdir}/%{java}/bin/appletviewer
%{_libdir}/%{java}/bin/extcheck
%{_libdir}/%{java}/bin/idlj
%{_libdir}/%{java}/bin/jar
%{_libdir}/%{java}/bin/jarsigner
%{_libdir}/%{java}/bin/java
%{_libdir}/%{java}/bin/javac
%{_libdir}/%{java}/bin/javadoc
%{_libdir}/%{java}/bin/javah
%{_libdir}/%{java}/bin/javap
%{_libdir}/%{java}/bin/jdb
%{_libdir}/%{java}/bin/native2ascii
%{_libdir}/%{java}/bin/oldjavac
%{_libdir}/%{java}/bin/oldjdb
%{_libdir}/%{java}/bin/rmic
%{_libdir}/%{java}/bin/serialver
%{_libdir}/%{java}/bin/appletviewer_g
%{_libdir}/%{java}/bin/extcheck_g
%{_libdir}/%{java}/bin/idlj_g
%{_libdir}/%{java}/bin/jar_g
%{_libdir}/%{java}/bin/jarsigner_g
%{_libdir}/%{java}/bin/javac_g
%{_libdir}/%{java}/bin/javadoc_g
%{_libdir}/%{java}/bin/javah_g
%{_libdir}/%{java}/bin/javap_g
%{_libdir}/%{java}/bin/jdb_g
%{_libdir}/%{java}/bin/native2ascii_g
%{_libdir}/%{java}/bin/oldjavac_g
%{_libdir}/%{java}/bin/oldjdb_g
%{_libdir}/%{java}/bin/rmic_g
%{_libdir}/%{java}/bin/serialver_g
%attr(755,root,root) %{_libdir}/%{java}/bin/jwrapper
%attr(755,root,root) %{_libdir}/%{java}/bin/exe/*
%attr(755,root,root) %{_bindir}/appletviewer
%attr(755,root,root) %{_bindir}/extcheck
%attr(755,root,root) %{_bindir}/idlj
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/native2ascii
%attr(755,root,root) %{_bindir}/oldjavac
%attr(755,root,root) %{_bindir}/oldjdb
%attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/serialver
%attr(755,root,root) %{_bindir}/appletviewer_g
%attr(755,root,root) %{_bindir}/extcheck_g
%attr(755,root,root) %{_bindir}/idlj_g
%attr(755,root,root) %{_bindir}/jar_g
%attr(755,root,root) %{_bindir}/jarsigner_g
%attr(755,root,root) %{_bindir}/javac_g
%attr(755,root,root) %{_bindir}/javadoc_g
%attr(755,root,root) %{_bindir}/javah_g
%attr(755,root,root) %{_bindir}/javap_g
%attr(755,root,root) %{_bindir}/jdb_g
%attr(755,root,root) %{_bindir}/native2ascii_g
%attr(755,root,root) %{_bindir}/oldjavac_g
%attr(755,root,root) %{_bindir}/oldjdb_g
%attr(755,root,root) %{_bindir}/rmic_g
%attr(755,root,root) %{_bindir}/serialver_g

%attr(755,root,root) %{_libdir}/%{java}/jre/bin/exe/*
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/classic/*
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/*.so
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/java_vm*
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/jvmtcf*
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/java
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/java-rmi
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/javaw
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/keytool
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/oldjava
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/oldjavaw
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/policytool
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/rmid
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/rmiregistry
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/tnameserv
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/java_g
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/java-rmi_g
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/javaw_g
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/keytool_g
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/oldjava_g
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/oldjavaw_g
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/policytool_g
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/rmid_g
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/rmiregistry_g
%attr(755,root,root) %{_libdir}/%{java}/jre/bin/tnameserv_g

%{_libdir}/%{java}/jre/lib/*.properties*
%{_libdir}/%{java}/jre/lib/*.jar
%{_libdir}/%{java}/jre/lib/JavaPluginControlPanel
%{_libdir}/%{java}/jre/lib/tzmappings
%{_libdir}/%{java}/jre/lib/audio/*
%{_libdir}/%{java}/jre/lib/cmm/*
%{_libdir}/%{java}/jre/lib/ext/*
%{_libdir}/%{java}/jre/lib/fonts/*
%{_libdir}/%{java}/jre/lib/security/*
%{_libdir}/%{java}/jre/lib/images/*.gif
%{_libdir}/%{java}/jre/lib/images/*.jpg
%{_libdir}/%{java}/jre/lib/images/cursors/*
%{_libdir}/%{java}/jre/lib/images/ftp/*
%dir %{_libdir}/%{java}/jre/lib/locale/*
