
%define java	IBMJava2-14

%define __spec_install_post exit 0

Summary:	IBM Java Software Development Kit v1.4
Summary(pl):	Java SDK produkcji IBM
Name:		ibm-java-sdk
Version:	1.4
Release:	0.1
License:	Look into documentation
Group:		Development/Languages/Java
URL:		http://www.ibm.com/developer/java/
# http://www-106.ibm.com/developerworks/java/jdk/linux140/devkit-info.html
Source0:	IBMJava2-SDK-14.tgz
Provides:	jdk = %{version}
Obsoletes:	jdk
ExclusiveArch:	%{ix86}
BuildRequires:	file
Requires:	ibm-java-jre = %{version}
Requires:	fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%define         javadir         %{_libdir}/java
%define         jredir          %{_libdir}/java/jre
%define         javasrcdir      %{_libdir}/java
%define         javaincludedir      %{_libdir}/java/include
%define         classdir        %{_datadir}/java
%define         netscape4dir    /usr/%{_lib}/netscape
%define         mozilladir      /usr/%{_lib}/mozilla

%description
This is IBM's Java 1.4 SDK.

%description -l pl
Pakiet zawiera SDK Javy 1.4 firmy IBM.


%package -n ibm-java-jre
Summary:	IBM JRE (Java Runtime Environment) for Linux
Summary(pl):	IBM JRE - ¶rodowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Provides:	java1.4
Provides:	jre = %{version}
Provides:	java
Requires:	java-shared
Obsoletes:	java
Obsoletes:	jre

%description -n ibm-java-jre
Java Runtime Environment for Linux.

%description -n ibm-java-jre -l pl
¦rodowisko uruchomieniowe Javy dla Linuksa.


%package demos
Summary:	IBM's JDK demonstration programs
Summary(pl):	Programy demonstracyjne do JDK firmy IBM
Group:		Development/Languages/Java
Requires:	%{name} = %{version}

%description demos
JDK demonstration programs.

%description demos -l pl
Programy demonstracyjne do JDK.


%package src
Summary:	IBM's JDK source code
Summary(pl):	Programy demonstracyjne do JDK firmy IBM
Group:		Development/Languages/Java
Requires:	%{name} = %{version}

%description src
JDK source code.

%description src -l pl
Kod ¼ród³owy do JDK.


%package -n ibm-java-tools
Summary:	Shared java tools by IBM
Summary(pl):	Wspó³dzielone narzêdzia javy firmy IBM
Group:		Development/Languages/Java
Provides:	jar
Provides:	java-shared
Obsoletes:	java-shared
Obsoletes:	jar
Obsoletes:	fastjar

%description -n ibm-java-tools
This package contains tools that are common for every Java(tm)
implementation, such as rmic or jar.

%description -n ibm-java-tools -l pl
Pakiet ten zawiera narzêdzia wspólne dla ka¿dej implementacji
Javy(tm), takie jak rmic czy jar.


%package -n netscape4-plugin-java-ibm
Summary:	Netscape 4.x Java plugin (by IBM)
Summary(pl):	Wtyczka Javy do Netscape 4.x (firmy IBM)
Group:		Development/Languages/Java
Requires:	ibm-java-jre = %{version}
Requires:	netscape-common >= 4.0
Obsoletes:	blackdown-java-sdk-netscape4-plugin
Obsoletes:	netscape4-plugin-java-blackdown
Obsoletes:	java-sun-nn4-plugin
Obsoletes:	jre-netscape4-plugin

%description -n netscape4-plugin-java-ibm
Java plugin for Netscape 4.x.

%description -n netscape4-plugin-java-ibm -l pl
Wtyczka z obs³ug± Javy dla Netscape 4.x.

%package -n mozilla-plugin-java-ibm
Summary:	Mozilla Java plugin (by IBM)
Summary(pl):	Wtyczka Javy do Mozilli (firmy IBM)
Group:		Development/Languages/Java
Requires:	jre = %{version}
Prereq:		mozilla-embedded
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	java-sun-moz-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-java-blackdown

%description -n mozilla-plugin-java-ibm
Java plugin for Mozilla.

%description -n mozilla-plugin-java-ibm -l pl
Wtyczka z obs³ug± Javy dla Mozilli.

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

%defattr(755,root,root)
%{javadir}/bin/appletviewer
%{javadir}/bin/appletviewer_g
%{javadir}/bin/extcheck
%{javadir}/bin/extcheck_g
%{javadir}/bin/HtmlConverter
%{javadir}/bin/idlj
%{javadir}/bin/idlj_g
%{javadir}/bin/jarsigner
%{javadir}/bin/jarsigner_g
%{javadir}/bin/javac
%{javadir}/bin/javac_g
%{javadir}/bin/javadoc
%{javadir}/bin/javadoc_g
%{javadir}/bin/javah
%{javadir}/bin/javah_g
%{javadir}/bin/javap
%{javadir}/bin/javap_g
%{javadir}/bin/java-rmi.cgi
%{javadir}/bin/jdb
%{javadir}/bin/jdb_g
%{javadir}/bin/native2ascii
%{javadir}/bin/native2ascii_g
%{javadir}/bin/serialver
%{javadir}/bin/serialver_g



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

%defattr(755,root,root)
%{jredir}/bin/classic/*
%{jredir}/bin/*.properties
%{jredir}/bin/libawt_g.so
%{jredir}/bin/libawt.so
%{jredir}/bin/libcmm_g.so
%{jredir}/bin/libcmm.so
%{jredir}/bin/libdcpr_g.so
%{jredir}/bin/libdcpr.so
%{jredir}/bin/libdt_socket_g.so
%{jredir}/bin/libdt_socket.so
%{jredir}/bin/libfontmanager_g.so
%{jredir}/bin/libfontmanager.so
%{jredir}/bin/libhpi_g.so
%{jredir}/bin/libhpi.so
%{jredir}/bin/libhprof_g.so
%{jredir}/bin/libhprof.so
%{jredir}/bin/libjaas_g.so
%{jredir}/bin/libjaas.so
%{jredir}/bin/libjava_g.so
%{jredir}/bin/libjavaplugin_jni_g.so
%{jredir}/bin/libjavaplugin_jni.so
%{jredir}/bin/libjava.so
%{jredir}/bin/libjawt_g.so
%{jredir}/bin/libjawt.so
%{jredir}/bin/libjdwp_g.so
%{jredir}/bin/libjdwp.so
%{jredir}/bin/libjitc_g.so
%{jredir}/bin/libjitc.so
%{jredir}/bin/libjpeg_g.so
%{jredir}/bin/libjpeg.so
%{jredir}/bin/libjsound_g.so
%{jredir}/bin/libjsound.so
%{jredir}/bin/libnet_g.so
%{jredir}/bin/libnet.so
%{jredir}/bin/libnio_g.so
%{jredir}/bin/libnio.so
%{jredir}/bin/liborb_g.so
%{jredir}/bin/liborb.so
%{jredir}/bin/librmi_g.so
%{jredir}/bin/librmi.so
%{jredir}/bin/libxhpi_g.so
%{jredir}/bin/libxhpi.so
%{jredir}/bin/libzip_g.so
%{jredir}/bin/libzip.so
%{jredir}/bin/awt_robot
%{jredir}/bin/awt_robot_g
%{jredir}/bin/java
%{jredir}/bin/java_g
%{jredir}/bin/JavaPluginControlPanel
%{jredir}/bin/javaw
%{jredir}/bin/javaw_g
%{jredir}/bin/jvmdcf
%{jredir}/bin/jvmdcf_g
%{jredir}/bin/jvmtcf
%{jredir}/bin/jvmtcf_g
%{jredir}/bin/keytool
%{jredir}/bin/keytool_g
%{jredir}/bin/policytool
%{jredir}/bin/policytool_g
%{jredir}/bin/rmid
%{jredir}/bin/rmid_g
%{jredir}/bin/tnameserv
%{jredir}/bin/tnameserv_g
%{jredir}/bin/webstart_install.sh


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
%defattr(755,root,root)
%{javadir}/bin/java
%{javadir}/bin/java_g
%{javadir}/bin/javaw
%{javadir}/bin/javaw_g
%{javadir}/bin/jvmtcf
%{javadir}/bin/jvmtcf_g
%{javadir}/bin/keytool
%{javadir}/bin/keytool_g
%{javadir}/bin/policytool
%{javadir}/bin/policytool_g
%{javadir}/bin/rmid
%{javadir}/bin/rmid_g
%{javadir}/bin/tnameserv
%{javadir}/bin/tnameserv_g


%files -n %{name}-demos
%defattr(644,root,root,755)
%dir %{javadir}/demo
%{javadir}/demo/*

%files -n %{name}-src
%defattr(644,root,root,755)
%{javadir}/src.jar

%files -n ibm-java-tools
%defattr(755,root,root)
%{javadir}/bin/jar
%{javadir}/bin/jar_g
%{_bindir}/jar
%{_bindir}/jar_g

%{javadir}/bin/rmiregistry
%{javadir}/bin/rmiregistry_g
%{_bindir}/rmiregistry
%{_bindir}/rmiregistry_g
%{jredir}/bin/rmiregistry
%{jredir}/bin/rmiregistry_g

%{javadir}/bin/rmic
%{javadir}/bin/rmic_g
%{_bindir}/rmic
%{_bindir}/rmic_g

%files -n netscape4-plugin-java-ibm
%defattr(644,root,root,755)
%{netscape4dir}/plugins/*

%files -n mozilla-plugin-java-ibm
%defattr(644,root,root,755)
%{mozilladir}/plugins/libjavaplugin_oji.so
%{jredir}/bin/libjavaplugin_oji.so
%{jredir}/bin/libjavaplugin_oji_g.so
