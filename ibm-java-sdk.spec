%define		__spec_install_post	exit 0
%define		halfname		ibm-java-sdk
%define		ver			1.3

Summary:	IBM Java Software Development Kit v1.3
Summary(pl):	Java SDK produkcji IBM
Name:		%{halfname}-%{ver}
Version:	0
Release:	1
License:	Look into documentation
Group:		Development/Languages/Java
Source0:	IBMJava2-SDK-13.tgz
Source1:	%{halfname}-wrapper.sh
URL:		http://www.ibm.com/developer/java/
Provides:	jdk = %{ver}
Provides:	jre = %{ver}
Provides:	jar
Conflicts:	kaffe
ExclusiveArch:	%{ix86}
BuildRequires:	file
Requires:	which
Requires:	fileutils
PreReq:		java-env
Requires:	java-env
Requires(post,preun,postun): java-env
BuildRequires:	java-env
Obsoletes:	ibm-java-%{ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		java		IBMJava2-13
%define		javadir		%{_libdir}/%{name}
%define		netscape4dir	%{_libdir}/netscape
%define		javacfgdir	/etc/sysconfig/java

%description
This is IBM's Java 1.3 SDK.

%description -l pl
Pakiet zawiera SDK Javy 1.3 firmy IBM.

%package netscape4-plugin
Summary:	Netscape 4.x Java plugin
Summary(pl):	Plugin Javy do Netscape 4.x
Group:		Development/Languages/Java
Requires:	jre = %{ver}
Requires:	netscape-common >= 4.0

%description netscape4-plugin
Java plugin for Netscape 4.x.

%description netscape4-plugin -l pl
Wtyczka z obs³ug± Javy dla Netscape 4.x.

%prep
%setup -q -n %{java}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{javadir}/{bin,jre/bin/classic,include} \
	$RPM_BUILD_ROOT%{netscape4dir}/plugins \
	$RPM_BUILD_ROOT%{javacfgdir}

cp -a bin/exe $RPM_BUILD_ROOT%{javadir}/bin/
cp -a jre/bin/exe $RPM_BUILD_ROOT%{javadir}/jre/bin/
cp -a lib $RPM_BUILD_ROOT%{javadir}/
cp -a jre/lib $RPM_BUILD_ROOT%{javadir}/jre/

install %{SOURCE1} $RPM_BUILD_ROOT%{javadir}/bin/jwrapper

install jre/bin/*.so $RPM_BUILD_ROOT%{javadir}/jre/bin
#install jre/bin/java_vm* $RPM_BUILD_ROOT%{_libdir}/%{java}/jre/bin
install jre/bin/jvmtcf* $RPM_BUILD_ROOT%{javadir}/jre/bin
install jre/bin/classic/*.so $RPM_BUILD_ROOT%{javadir}/jre/bin/classic/
install include/* $RPM_BUILD_ROOT%{javadir}/include
ln -sf %{javadir}/jre/bin/javaplugin.so $RPM_BUILD_ROOT%{netscape4dir}/plugins/javaplugin.so

for i in bin/*; do
	file $i | grep -q "shell" && \
	ln -sf %{javadir}/bin/jwrapper \
		$RPM_BUILD_ROOT%{javadir}/$i
done

for i in jre/bin/*; do
	file $i | grep -q "shell" && \
	ln -sf %{javadir}/bin/jwrapper \
		$RPM_BUILD_ROOT%{javadir}/$i
done
rm -f $RPM_BUILD_ROOT%{javadir}/bin/java
ln -sf ../jre/bin/java $RPM_BUILD_ROOT%{javadir}/bin/java

# create some config files
echo "MAINDIR=%{name}" > $RPM_BUILD_ROOT%{javacfgdir}/jdk.%{name}

%define	lnfile	$RPM_BUILD_ROOT%{javacfgdir}/links.jdk.%{name}

echo "%{javadir} %{_libdir}/java" 		>> %{lnfile}
echo "%{javadir} %{_libdir}/java-jre" 		>> %{lnfile}
echo "%{javadir} %{_libdir}/java-sdk" 		>> %{lnfile}
echo "%{javadir}/include %{_includedir}/jdk" 	>> %{lnfile}

for i in bin/*; do
	nbin=`basename $i`
	echo "%{javadir}/bin/$nbin %{_bindir}/$nbin" >> %{lnfile}
done

# cp files
javacpmgr --findjars $RPM_BUILD_ROOT > $RPM_BUILD_ROOT%{javacfgdir}/cp.jdk.%{name}
# end of config files creation

%clean
rm -rf $RPM_BUILD_ROOT

%post
javaenv --erasejavaif "jre.ibm-java-%{ver}"
javaenv --setjava

%preun
javaenv --erasejavaif "jdk.%{name}"

%postun
javaenv --setjava

%files
%defattr(644,root,root,755)
%doc docs/* javasrc.jar jre/bin/classic/Xusage.txt
%doc jre/lib/jvm.hprof.txt

%{javacfgdir}/jdk.%{name}
%{javacfgdir}/links.jdk.%{name}
%config(noreplace) %verify(not size mtime md5) %{javacfgdir}/cp.jdk.%{name}

%dir %{javadir}
%dir %{javadir}/lib
%{javadir}/lib/*
%{javadir}/include

%dir %{javadir}/bin
%{javadir}/bin/appletviewer
%{javadir}/bin/appletviewer_g
%{javadir}/bin/extcheck
%{javadir}/bin/extcheck_g
%{javadir}/bin/idlj
%{javadir}/bin/idlj_g
%{javadir}/bin/jar
%{javadir}/bin/jar_g
%{javadir}/bin/jarsigner
%{javadir}/bin/jarsigner_g
%{javadir}/bin/java
%{javadir}/bin/javac
%{javadir}/bin/javac_g
%{javadir}/bin/javadoc
%{javadir}/bin/javadoc_g
%{javadir}/bin/javah
%{javadir}/bin/javah_g
%{javadir}/bin/javap
%{javadir}/bin/javap_g
%{javadir}/bin/jdb
%{javadir}/bin/jdb_g
%{javadir}/bin/native2ascii
%{javadir}/bin/native2ascii_g
%{javadir}/bin/oldjavac
%{javadir}/bin/oldjavac_g
%{javadir}/bin/oldjdb
%{javadir}/bin/oldjdb_g
%{javadir}/bin/rmic
%{javadir}/bin/rmic_g
%{javadir}/bin/serialver
%{javadir}/bin/serialver_g

%attr(755,root,root) %{javadir}/bin/jwrapper
%dir %{javadir}/bin/exe
%attr(755,root,root) %{javadir}/bin/exe/*

%dir %{javadir}/jre
%dir %{javadir}/jre/bin
%dir %{javadir}/jre/bin/exe
%dir %{javadir}/jre/bin/classic
%attr(755,root,root) %{javadir}/jre/bin/exe/*
%attr(755,root,root) %{javadir}/jre/bin/classic/*
%attr(755,root,root) %{javadir}/jre/bin/lib*.so
%attr(755,root,root) %{javadir}/jre/bin/javaplugin_g.so
%attr(755,root,root) %{javadir}/jre/bin/java
%attr(755,root,root) %{javadir}/jre/bin/java_g
%attr(755,root,root) %{javadir}/jre/bin/javaw
%attr(755,root,root) %{javadir}/jre/bin/javaw_g
%attr(755,root,root) %{javadir}/jre/bin/jvmtcf*
%attr(755,root,root) %{javadir}/jre/bin/keytool
%attr(755,root,root) %{javadir}/jre/bin/keytool_g
%attr(755,root,root) %{javadir}/jre/bin/oldjava
%attr(755,root,root) %{javadir}/jre/bin/oldjava_g
%attr(755,root,root) %{javadir}/jre/bin/oldjavaw
%attr(755,root,root) %{javadir}/jre/bin/oldjavaw_g
%attr(755,root,root) %{javadir}/jre/bin/policytool
%attr(755,root,root) %{javadir}/jre/bin/policytool_g
%attr(755,root,root) %{javadir}/jre/bin/rmid
%attr(755,root,root) %{javadir}/jre/bin/rmid_g
%attr(755,root,root) %{javadir}/jre/bin/rmiregistry
%attr(755,root,root) %{javadir}/jre/bin/rmiregistry_g
%attr(755,root,root) %{javadir}/jre/bin/tnameserv
%attr(755,root,root) %{javadir}/jre/bin/tnameserv_g
#%attr(755,root,root) %{javadir}/jre/bin/java-rmi
#%attr(755,root,root) %{javadir}/jre/bin/java-rmi_g
#%attr(755,root,root) %{javadir}/jre/bin/java_vm*

%dir %{javadir}/jre/lib
%{javadir}/jre/lib/*.properties*
%{javadir}/jre/lib/*.jar
%{javadir}/jre/lib/*.txt
%{javadir}/jre/lib/JavaPluginControlPanel
%{javadir}/jre/lib/tzmappings
%{javadir}/jre/lib/audio
%{javadir}/jre/lib/cmm
%{javadir}/jre/lib/ext
%{javadir}/jre/lib/fonts
%{javadir}/jre/lib/security
%dir %{javadir}/jre/lib/images
%{javadir}/jre/lib/images/*.gif
%{javadir}/jre/lib/images/*.jpg
%{javadir}/jre/lib/images/cursors
%{javadir}/jre/lib/images/ftp
#%dir %{javadir}/jre/lib/locale/*

%files netscape4-plugin
%defattr(644,root,root,755)
%attr(755,root,root) %{javadir}/jre/bin/javaplugin.so
%{netscape4dir}
