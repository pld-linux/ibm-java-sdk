
%define	java			IBMJava2-14

%define	__spec_install_post	exit 0

Summary:	IBM Java Software Development Kit v1.4
Summary(pl.UTF-8):	Java SDK produkcji IBM
Name:		ibm-java-sdk
Version:	1.4
Release:	0.1
License:	Look into documentation
Group:		Development/Languages/Java
URL:		http://www.ibm.com/developer/java/
# http://www-106.ibm.com/developerworks/java/jdk/linux140/devkit-info.html
Source0:	IBMJava2-SDK-14.tgz
BuildRequires:	file
Requires:	fileutils
Requires:	ibm-java-jre = %{version}
Provides:	jdk = %{version}
Obsoletes:	jdk
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%define		javadir		%{_libdir}/java
%define		jredir		%{_libdir}/java/jre
%define		javasrcdir	%{_libdir}/java
%define		javaincludedir	%{_libdir}/java/include
%define		classdir	%{_datadir}/java
%define		netscape4dir	/usr/%{_lib}/netscape
%define		mozilladir	/usr/%{_lib}/mozilla

%description
This is IBM's Java 1.4 SDK.

%description -l pl.UTF-8
Pakiet zawiera SDK Javy 1.4 firmy IBM.


%package -n ibm-java-jre
Summary:	IBM JRE (Java Runtime Environment) for Linux
Summary(pl.UTF-8):	IBM JRE - środowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	java-shared
Provides:	java
Provides:	java1.4
Provides:	jre = %{version}
Obsoletes:	java
Obsoletes:	jre

%description -n ibm-java-jre
Java Runtime Environment for Linux.

%description -n ibm-java-jre -l pl.UTF-8
Środowisko uruchomieniowe Javy dla Linuksa.


%package demos
Summary:	IBM's JDK demonstration programs
Summary(pl.UTF-8):	Programy demonstracyjne do JDK firmy IBM
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description demos
JDK demonstration programs.

%description demos -l pl.UTF-8
Programy demonstracyjne do JDK.


%package src
Summary:	IBM's JDK source code
Summary(pl.UTF-8):	Programy demonstracyjne do JDK firmy IBM
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description src
JDK source code.

%description src -l pl.UTF-8
Kod źródłowy do JDK.


%package -n ibm-java-tools
Summary:	Shared java tools by IBM
Summary(pl.UTF-8):	Współdzielone narzędzia javy firmy IBM
Group:		Development/Languages/Java
Provides:	jar
Provides:	java-shared
Obsoletes:	fastjar
Obsoletes:	jar
Obsoletes:	java-shared

%description -n ibm-java-tools
This package contains tools that are common for every Java(tm)
implementation, such as rmic or jar.

%description -n ibm-java-tools -l pl.UTF-8
Pakiet ten zawiera narzędzia wspólne dla każdej implementacji
Javy(tm), takie jak rmic czy jar.


%package -n netscape4-plugin-java-ibm
Summary:	Netscape 4.x Java plugin (by IBM)
Summary(pl.UTF-8):	Wtyczka Javy do Netscape 4.x (firmy IBM)
Group:		Development/Languages/Java
Requires:	ibm-java-jre = %{version}
Requires:	netscape-common >= 4.0
Obsoletes:	blackdown-java-sdk-netscape4-plugin
Obsoletes:	java-sun-nn4-plugin
Obsoletes:	jre-netscape4-plugin
Obsoletes:	netscape4-plugin-java-blackdown

%description -n netscape4-plugin-java-ibm
Java plugin for Netscape 4.x.

%description -n netscape4-plugin-java-ibm -l pl.UTF-8
Wtyczka z obsługą Javy dla Netscape 4.x.

%package -n mozilla-plugin-java-ibm
Summary:	Mozilla Java plugin (by IBM)
Summary(pl.UTF-8):	Wtyczka Javy do Mozilli (firmy IBM)
Group:		Development/Languages/Java
Requires:	jre = %{version}
Requires:	mozilla-embedded
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	java-sun-moz-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-java-blackdown

%description -n mozilla-plugin-java-ibm
Java plugin for Mozilla.

%description -n mozilla-plugin-java-ibm -l pl.UTF-8
Wtyczka z obsługą Javy dla Mozilli.

%prep
%setup -q -n %{java}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{javadir}/{bin,jre/bin/classic} \
	$RPM_BUILD_ROOT%{netscape4dir}/plugins \
	$RPM_BUILD_ROOT%{mozilladir}/plugins \
	$RPM_BUILD_ROOT%{javaincludedir} \
	$RPM_BUILD_ROOT%{_bindir}


cp -a bin $RPM_BUILD_ROOT%{javadir}
cp -a lib $RPM_BUILD_ROOT%{javadir}

cp -a jre/bin $RPM_BUILD_ROOT%{jredir}
cp -a jre/lib $RPM_BUILD_ROOT%{jredir}

cp -a demo $RPM_BUILD_ROOT%{javadir}

for i in bin/*; do
	ln -sf %{javadir}/$i \
		$RPM_BUILD_ROOT%{_bindir}/"$( basename "$i" )"
done

ln -sf ../jre/bin/java $RPM_BUILD_ROOT%{javadir}/bin/java

install include/*.h $RPM_BUILD_ROOT%{javaincludedir}

# netscape plugin
mv $RPM_BUILD_ROOT%{jredir}/bin/javaplugin*.so \
	$RPM_BUILD_ROOT%{netscape4dir}/plugins

# mozilla plugin
ln -s %{jredir}/bin/libjavaplugin_oji.so \
	$RPM_BUILD_ROOT%{mozilladir}/plugins/libjavaplugin_oji.so

# src
install src.jar $RPM_BUILD_ROOT%{javasrcdir}

# goes to %%doc, not needed in {jredir}/lib
rm -f $RPM_BUILD_ROOT%{jredir}/lib/jvm.hprof.txt


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/sdk docs/readmefirst.lnxia32.txt docs/*.htm docs/COPYRIGHT

%dir %{javadir}/lib
%{javadir}/lib/*

%{javaincludedir}/*.h

%attr(755,root,root) %{_bindir}/appletviewer
%attr(755,root,root) %{_bindir}/appletviewer_g
%attr(755,root,root) %{_bindir}/extcheck
%attr(755,root,root) %{_bindir}/extcheck_g
%attr(755,root,root) %{_bindir}/HtmlConverter
%attr(755,root,root) %{_bindir}/idlj
%attr(755,root,root) %{_bindir}/idlj_g
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/jarsigner_g
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javac_g
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javadoc_g
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javah_g
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/javap_g
%attr(755,root,root) %{_bindir}/java-rmi.cgi
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/jdb_g
%attr(755,root,root) %{_bindir}/native2ascii
%attr(755,root,root) %{_bindir}/native2ascii_g
%attr(755,root,root) %{_bindir}/serialver
%attr(755,root,root) %{_bindir}/serialver_g

%attr(755,root,root) %{javadir}/bin/appletviewer
%attr(755,root,root) %{javadir}/bin/appletviewer_g
%attr(755,root,root) %{javadir}/bin/extcheck
%attr(755,root,root) %{javadir}/bin/extcheck_g
%attr(755,root,root) %{javadir}/bin/HtmlConverter
%attr(755,root,root) %{javadir}/bin/idlj
%attr(755,root,root) %{javadir}/bin/idlj_g
%attr(755,root,root) %{javadir}/bin/jarsigner
%attr(755,root,root) %{javadir}/bin/jarsigner_g
%attr(755,root,root) %{javadir}/bin/javac
%attr(755,root,root) %{javadir}/bin/javac_g
%attr(755,root,root) %{javadir}/bin/javadoc
%attr(755,root,root) %{javadir}/bin/javadoc_g
%attr(755,root,root) %{javadir}/bin/javah
%attr(755,root,root) %{javadir}/bin/javah_g
%attr(755,root,root) %{javadir}/bin/javap
%attr(755,root,root) %{javadir}/bin/javap_g
%attr(755,root,root) %{javadir}/bin/java-rmi.cgi
%attr(755,root,root) %{javadir}/bin/jdb
%attr(755,root,root) %{javadir}/bin/jdb_g
%attr(755,root,root) %{javadir}/bin/native2ascii
%attr(755,root,root) %{javadir}/bin/native2ascii_g
%attr(755,root,root) %{javadir}/bin/serialver
%attr(755,root,root) %{javadir}/bin/serialver_g



%files -n ibm-java-jre
%defattr(644,root,root,755)
%doc docs/jaas docs/jre docs/rmi-iiop
%doc jre/lib/jvm.hprof.txt

%dir %{javadir}

%dir %{jredir}/lib
%{jredir}/lib/*


%dir %{jredir}
%dir %{jredir}/bin
%dir %{jredir}/bin/classic

%attr(755,root,root) %{jredir}/bin/classic/*
%attr(755,root,root) %{jredir}/bin/*.properties
%attr(755,root,root) %{jredir}/bin/libawt_g.so
%attr(755,root,root) %{jredir}/bin/libawt.so
%attr(755,root,root) %{jredir}/bin/libcmm_g.so
%attr(755,root,root) %{jredir}/bin/libcmm.so
%attr(755,root,root) %{jredir}/bin/libdcpr_g.so
%attr(755,root,root) %{jredir}/bin/libdcpr.so
%attr(755,root,root) %{jredir}/bin/libdt_socket_g.so
%attr(755,root,root) %{jredir}/bin/libdt_socket.so
%attr(755,root,root) %{jredir}/bin/libfontmanager_g.so
%attr(755,root,root) %{jredir}/bin/libfontmanager.so
%attr(755,root,root) %{jredir}/bin/libhpi_g.so
%attr(755,root,root) %{jredir}/bin/libhpi.so
%attr(755,root,root) %{jredir}/bin/libhprof_g.so
%attr(755,root,root) %{jredir}/bin/libhprof.so
%attr(755,root,root) %{jredir}/bin/libjaas_g.so
%attr(755,root,root) %{jredir}/bin/libjaas.so
%attr(755,root,root) %{jredir}/bin/libjava_g.so
%attr(755,root,root) %{jredir}/bin/libjavaplugin_jni_g.so
%attr(755,root,root) %{jredir}/bin/libjavaplugin_jni.so
%attr(755,root,root) %{jredir}/bin/libjava.so
%attr(755,root,root) %{jredir}/bin/libjawt_g.so
%attr(755,root,root) %{jredir}/bin/libjawt.so
%attr(755,root,root) %{jredir}/bin/libjdwp_g.so
%attr(755,root,root) %{jredir}/bin/libjdwp.so
%attr(755,root,root) %{jredir}/bin/libjitc_g.so
%attr(755,root,root) %{jredir}/bin/libjitc.so
%attr(755,root,root) %{jredir}/bin/libjpeg_g.so
%attr(755,root,root) %{jredir}/bin/libjpeg.so
%attr(755,root,root) %{jredir}/bin/libjsound_g.so
%attr(755,root,root) %{jredir}/bin/libjsound.so
%attr(755,root,root) %{jredir}/bin/libnet_g.so
%attr(755,root,root) %{jredir}/bin/libnet.so
%attr(755,root,root) %{jredir}/bin/libnio_g.so
%attr(755,root,root) %{jredir}/bin/libnio.so
%attr(755,root,root) %{jredir}/bin/liborb_g.so
%attr(755,root,root) %{jredir}/bin/liborb.so
%attr(755,root,root) %{jredir}/bin/librmi_g.so
%attr(755,root,root) %{jredir}/bin/librmi.so
%attr(755,root,root) %{jredir}/bin/libxhpi_g.so
%attr(755,root,root) %{jredir}/bin/libxhpi.so
%attr(755,root,root) %{jredir}/bin/libzip_g.so
%attr(755,root,root) %{jredir}/bin/libzip.so
%attr(755,root,root) %{jredir}/bin/awt_robot
%attr(755,root,root) %{jredir}/bin/awt_robot_g
%attr(755,root,root) %{jredir}/bin/java
%attr(755,root,root) %{jredir}/bin/java_g
%attr(755,root,root) %{jredir}/bin/JavaPluginControlPanel
%attr(755,root,root) %{jredir}/bin/javaw
%attr(755,root,root) %{jredir}/bin/javaw_g
%attr(755,root,root) %{jredir}/bin/jvmdcf
%attr(755,root,root) %{jredir}/bin/jvmdcf_g
%attr(755,root,root) %{jredir}/bin/jvmtcf
%attr(755,root,root) %{jredir}/bin/jvmtcf_g
%attr(755,root,root) %{jredir}/bin/keytool
%attr(755,root,root) %{jredir}/bin/keytool_g
%attr(755,root,root) %{jredir}/bin/policytool
%attr(755,root,root) %{jredir}/bin/policytool_g
%attr(755,root,root) %{jredir}/bin/rmid
%attr(755,root,root) %{jredir}/bin/rmid_g
%attr(755,root,root) %{jredir}/bin/tnameserv
%attr(755,root,root) %{jredir}/bin/tnameserv_g
%attr(755,root,root) %{jredir}/bin/webstart_install.sh


%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/java_g
%attr(755,root,root) %{_bindir}/javaw
%attr(755,root,root) %{_bindir}/javaw_g
%attr(755,root,root) %{_bindir}/jvmtcf
%attr(755,root,root) %{_bindir}/jvmtcf_g
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/keytool_g
%attr(755,root,root) %{_bindir}/policytool
%attr(755,root,root) %{_bindir}/policytool_g
%attr(755,root,root) %{_bindir}/rmid
%attr(755,root,root) %{_bindir}/rmid_g
%attr(755,root,root) %{_bindir}/tnameserv
%attr(755,root,root) %{_bindir}/tnameserv_g

%dir %{javadir}/bin
%attr(755,root,root) %{javadir}/bin/java
%attr(755,root,root) %{javadir}/bin/java_g
%attr(755,root,root) %{javadir}/bin/javaw
%attr(755,root,root) %{javadir}/bin/javaw_g
%attr(755,root,root) %{javadir}/bin/jvmtcf
%attr(755,root,root) %{javadir}/bin/jvmtcf_g
%attr(755,root,root) %{javadir}/bin/keytool
%attr(755,root,root) %{javadir}/bin/keytool_g
%attr(755,root,root) %{javadir}/bin/policytool
%attr(755,root,root) %{javadir}/bin/policytool_g
%attr(755,root,root) %{javadir}/bin/rmid
%attr(755,root,root) %{javadir}/bin/rmid_g
%attr(755,root,root) %{javadir}/bin/tnameserv
%attr(755,root,root) %{javadir}/bin/tnameserv_g


%files -n %{name}-demos
%defattr(644,root,root,755)
%dir %{javadir}/demo
%{javadir}/demo/*

%files -n %{name}-src
%defattr(644,root,root,755)
%{javadir}/src.jar

%files -n ibm-java-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{javadir}/bin/jar
%attr(755,root,root) %{javadir}/bin/jar_g
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/jar_g

%attr(755,root,root) %{javadir}/bin/rmiregistry
%attr(755,root,root) %{javadir}/bin/rmiregistry_g
%attr(755,root,root) %{_bindir}/rmiregistry
%attr(755,root,root) %{_bindir}/rmiregistry_g
%attr(755,root,root) %{jredir}/bin/rmiregistry
%attr(755,root,root) %{jredir}/bin/rmiregistry_g

%attr(755,root,root) %{javadir}/bin/rmic
%attr(755,root,root) %{javadir}/bin/rmic_g
%attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/rmic_g

%files -n netscape4-plugin-java-ibm
%defattr(644,root,root,755)
%{netscape4dir}/plugins/*

%files -n mozilla-plugin-java-ibm
%defattr(644,root,root,755)
%{mozilladir}/plugins/libjavaplugin_oji.so
%{jredir}/bin/libjavaplugin_oji.so
%{jredir}/bin/libjavaplugin_oji_g.so
