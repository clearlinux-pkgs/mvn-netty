#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-netty
Version  : 3.10.6.final
Release  : 8
URL      : https://repo1.maven.org/maven2/io/netty/netty/3.10.6.Final/netty-3.10.6.Final.jar
Source0  : https://repo1.maven.org/maven2/io/netty/netty/3.10.6.Final/netty-3.10.6.Final.jar
Source1  : https://repo.maven.apache.org/maven2/io/netty/netty-all/4.0.44.Final/netty-all-4.0.44.Final-sources.jar
Source2  : https://repo.maven.apache.org/maven2/io/netty/netty-all/4.0.44.Final/netty-all-4.0.44.Final.jar
Source3  : https://repo.maven.apache.org/maven2/io/netty/netty-all/4.0.44.Final/netty-all-4.0.44.Final.pom
Source4  : https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.0.44.Final/netty-parent-4.0.44.Final.pom
Source5  : https://repo1.maven.org/maven2/io/netty/netty-all/4.0.23.Final/netty-all-4.0.23.Final.jar
Source6  : https://repo1.maven.org/maven2/io/netty/netty-all/4.0.23.Final/netty-all-4.0.23.Final.pom
Source7  : https://repo1.maven.org/maven2/io/netty/netty-all/4.0.52.Final/netty-all-4.0.52.Final.jar
Source8  : https://repo1.maven.org/maven2/io/netty/netty-all/4.0.52.Final/netty-all-4.0.52.Final.pom
Source9  : https://repo1.maven.org/maven2/io/netty/netty-all/4.1.17.Final/netty-all-4.1.17.Final.jar
Source10  : https://repo1.maven.org/maven2/io/netty/netty-all/4.1.17.Final/netty-all-4.1.17.Final.pom
Source11  : https://repo1.maven.org/maven2/io/netty/netty-all/4.1.8.Final/netty-all-4.1.8.Final.jar
Source12  : https://repo1.maven.org/maven2/io/netty/netty-all/4.1.8.Final/netty-all-4.1.8.Final.pom
Source13  : https://repo1.maven.org/maven2/io/netty/netty-codec-socks/4.0.24.Final/netty-codec-socks-4.0.24.Final.jar
Source14  : https://repo1.maven.org/maven2/io/netty/netty-codec-socks/4.0.24.Final/netty-codec-socks-4.0.24.Final.pom
Source15  : https://repo1.maven.org/maven2/io/netty/netty-parent/4.0.23.Final/netty-parent-4.0.23.Final.pom
Source16  : https://repo1.maven.org/maven2/io/netty/netty-parent/4.0.24.Final/netty-parent-4.0.24.Final.pom
Source17  : https://repo1.maven.org/maven2/io/netty/netty-parent/4.0.33.Final/netty-parent-4.0.33.Final.pom
Source18  : https://repo1.maven.org/maven2/io/netty/netty-parent/4.0.52.Final/netty-parent-4.0.52.Final.pom
Source19  : https://repo1.maven.org/maven2/io/netty/netty-parent/4.1.13.Final/netty-parent-4.1.13.Final.pom
Source20  : https://repo1.maven.org/maven2/io/netty/netty-parent/4.1.16.Final/netty-parent-4.1.16.Final.pom
Source21  : https://repo1.maven.org/maven2/io/netty/netty-parent/4.1.17.Final/netty-parent-4.1.17.Final.pom
Source22  : https://repo1.maven.org/maven2/io/netty/netty-parent/4.1.6.Final/netty-parent-4.1.6.Final.pom
Source23  : https://repo1.maven.org/maven2/io/netty/netty-parent/4.1.8.Final/netty-parent-4.1.8.Final.pom
Source24  : https://repo1.maven.org/maven2/io/netty/netty/3.10.5.Final/netty-3.10.5.Final.jar
Source25  : https://repo1.maven.org/maven2/io/netty/netty/3.10.5.Final/netty-3.10.5.Final.pom
Source26  : https://repo1.maven.org/maven2/io/netty/netty/3.10.6.Final/netty-3.10.6.Final.pom
Source27  : https://repo1.maven.org/maven2/io/netty/netty/3.4.0.Final/netty-3.4.0.Final.jar
Source28  : https://repo1.maven.org/maven2/io/netty/netty/3.4.0.Final/netty-3.4.0.Final.pom
Source29  : https://repo1.maven.org/maven2/io/netty/netty/3.6.2.Final/netty-3.6.2.Final.jar
Source30  : https://repo1.maven.org/maven2/io/netty/netty/3.6.2.Final/netty-3.6.2.Final.pom
Source31  : https://repo1.maven.org/maven2/io/netty/netty/3.7.0.Final/netty-3.7.0.Final.jar
Source32  : https://repo1.maven.org/maven2/io/netty/netty/3.7.0.Final/netty-3.7.0.Final.pom
Source33  : https://repo1.maven.org/maven2/io/netty/netty/3.9.9.Final/netty-3.9.9.Final.jar
Source34  : https://repo1.maven.org/maven2/io/netty/netty/3.9.9.Final/netty-3.9.9.Final.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause LGPL-2.1 MIT Public-Domain
Requires: mvn-netty-data = %{version}-%{release}
Requires: mvn-netty-license = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-netty package.
Group: Data

%description data
data components for the mvn-netty package.


%package license
Summary: license components for the mvn-netty package.
Group: Default

%description license
license components for the mvn-netty package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-netty
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-netty/LICENSE.txt
cp license/LICENSE.base64.txt %{buildroot}/usr/share/package-licenses/mvn-netty/license_LICENSE.base64.txt
cp license/LICENSE.bouncycastle.txt %{buildroot}/usr/share/package-licenses/mvn-netty/license_LICENSE.bouncycastle.txt
cp license/LICENSE.commons-logging.txt %{buildroot}/usr/share/package-licenses/mvn-netty/license_LICENSE.commons-logging.txt
cp license/LICENSE.felix.txt %{buildroot}/usr/share/package-licenses/mvn-netty/license_LICENSE.felix.txt
cp license/LICENSE.jboss-logging.txt %{buildroot}/usr/share/package-licenses/mvn-netty/license_LICENSE.jboss-logging.txt
cp license/LICENSE.jsr166y.txt %{buildroot}/usr/share/package-licenses/mvn-netty/license_LICENSE.jsr166y.txt
cp license/LICENSE.jzlib.txt %{buildroot}/usr/share/package-licenses/mvn-netty/license_LICENSE.jzlib.txt
cp license/LICENSE.log4j.txt %{buildroot}/usr/share/package-licenses/mvn-netty/license_LICENSE.log4j.txt
cp license/LICENSE.protobuf.txt %{buildroot}/usr/share/package-licenses/mvn-netty/license_LICENSE.protobuf.txt
cp license/LICENSE.slf4j.txt %{buildroot}/usr/share/package-licenses/mvn-netty/license_LICENSE.slf4j.txt
cp license/LICENSE.webbit.txt %{buildroot}/usr/share/package-licenses/mvn-netty/license_LICENSE.webbit.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.10.6.Final
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.10.6.Final/netty-3.10.6.Final.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.44.Final
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.44.Final/netty-all-4.0.44.Final-sources.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.44.Final
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.44.Final/netty-all-4.0.44.Final.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.44.Final
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.44.Final/netty-all-4.0.44.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.44.Final
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.44.Final/netty-parent-4.0.44.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.23.Final
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.23.Final/netty-all-4.0.23.Final.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.23.Final
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.23.Final/netty-all-4.0.23.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.52.Final
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.52.Final/netty-all-4.0.52.Final.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.52.Final
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.0.52.Final/netty-all-4.0.52.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.1.17.Final
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.1.17.Final/netty-all-4.1.17.Final.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.1.17.Final
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.1.17.Final/netty-all-4.1.17.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.1.8.Final
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.1.8.Final/netty-all-4.1.8.Final.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.1.8.Final
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-all/4.1.8.Final/netty-all-4.1.8.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-codec-socks/4.0.24.Final
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-codec-socks/4.0.24.Final/netty-codec-socks-4.0.24.Final.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-codec-socks/4.0.24.Final
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-codec-socks/4.0.24.Final/netty-codec-socks-4.0.24.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.23.Final
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.23.Final/netty-parent-4.0.23.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.24.Final
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.24.Final/netty-parent-4.0.24.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.33.Final
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.33.Final/netty-parent-4.0.33.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.52.Final
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.52.Final/netty-parent-4.0.52.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.13.Final
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.13.Final/netty-parent-4.1.13.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.16.Final
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.16.Final/netty-parent-4.1.16.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.17.Final
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.17.Final/netty-parent-4.1.17.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.6.Final
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.6.Final/netty-parent-4.1.6.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.8.Final
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.8.Final/netty-parent-4.1.8.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.10.5.Final
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.10.5.Final/netty-3.10.5.Final.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.10.5.Final
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.10.5.Final/netty-3.10.5.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.10.6.Final
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.10.6.Final/netty-3.10.6.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.4.0.Final
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.4.0.Final/netty-3.4.0.Final.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.4.0.Final
cp %{SOURCE28} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.4.0.Final/netty-3.4.0.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.6.2.Final
cp %{SOURCE29} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.6.2.Final/netty-3.6.2.Final.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.6.2.Final
cp %{SOURCE30} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.6.2.Final/netty-3.6.2.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.7.0.Final
cp %{SOURCE31} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.7.0.Final/netty-3.7.0.Final.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.7.0.Final
cp %{SOURCE32} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.7.0.Final/netty-3.7.0.Final.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.9.9.Final
cp %{SOURCE33} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.9.9.Final/netty-3.9.9.Final.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.9.9.Final
cp %{SOURCE34} %{buildroot}/usr/share/java/.m2/repository/io/netty/netty/3.9.9.Final/netty-3.9.9.Final.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/io/netty/netty-all/4.0.23.Final/netty-all-4.0.23.Final.jar
/usr/share/java/.m2/repository/io/netty/netty-all/4.0.23.Final/netty-all-4.0.23.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-all/4.0.44.Final/netty-all-4.0.44.Final-sources.jar
/usr/share/java/.m2/repository/io/netty/netty-all/4.0.44.Final/netty-all-4.0.44.Final.jar
/usr/share/java/.m2/repository/io/netty/netty-all/4.0.44.Final/netty-all-4.0.44.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-all/4.0.52.Final/netty-all-4.0.52.Final.jar
/usr/share/java/.m2/repository/io/netty/netty-all/4.0.52.Final/netty-all-4.0.52.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-all/4.1.17.Final/netty-all-4.1.17.Final.jar
/usr/share/java/.m2/repository/io/netty/netty-all/4.1.17.Final/netty-all-4.1.17.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-all/4.1.8.Final/netty-all-4.1.8.Final.jar
/usr/share/java/.m2/repository/io/netty/netty-all/4.1.8.Final/netty-all-4.1.8.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-codec-socks/4.0.24.Final/netty-codec-socks-4.0.24.Final.jar
/usr/share/java/.m2/repository/io/netty/netty-codec-socks/4.0.24.Final/netty-codec-socks-4.0.24.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.23.Final/netty-parent-4.0.23.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.24.Final/netty-parent-4.0.24.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.33.Final/netty-parent-4.0.33.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.44.Final/netty-parent-4.0.44.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-parent/4.0.52.Final/netty-parent-4.0.52.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.13.Final/netty-parent-4.1.13.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.16.Final/netty-parent-4.1.16.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.17.Final/netty-parent-4.1.17.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.6.Final/netty-parent-4.1.6.Final.pom
/usr/share/java/.m2/repository/io/netty/netty-parent/4.1.8.Final/netty-parent-4.1.8.Final.pom
/usr/share/java/.m2/repository/io/netty/netty/3.10.5.Final/netty-3.10.5.Final.jar
/usr/share/java/.m2/repository/io/netty/netty/3.10.5.Final/netty-3.10.5.Final.pom
/usr/share/java/.m2/repository/io/netty/netty/3.10.6.Final/netty-3.10.6.Final.jar
/usr/share/java/.m2/repository/io/netty/netty/3.10.6.Final/netty-3.10.6.Final.pom
/usr/share/java/.m2/repository/io/netty/netty/3.4.0.Final/netty-3.4.0.Final.jar
/usr/share/java/.m2/repository/io/netty/netty/3.4.0.Final/netty-3.4.0.Final.pom
/usr/share/java/.m2/repository/io/netty/netty/3.6.2.Final/netty-3.6.2.Final.jar
/usr/share/java/.m2/repository/io/netty/netty/3.6.2.Final/netty-3.6.2.Final.pom
/usr/share/java/.m2/repository/io/netty/netty/3.7.0.Final/netty-3.7.0.Final.jar
/usr/share/java/.m2/repository/io/netty/netty/3.7.0.Final/netty-3.7.0.Final.pom
/usr/share/java/.m2/repository/io/netty/netty/3.9.9.Final/netty-3.9.9.Final.jar
/usr/share/java/.m2/repository/io/netty/netty/3.9.9.Final/netty-3.9.9.Final.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-netty/LICENSE.txt
/usr/share/package-licenses/mvn-netty/license_LICENSE.base64.txt
/usr/share/package-licenses/mvn-netty/license_LICENSE.bouncycastle.txt
/usr/share/package-licenses/mvn-netty/license_LICENSE.commons-logging.txt
/usr/share/package-licenses/mvn-netty/license_LICENSE.felix.txt
/usr/share/package-licenses/mvn-netty/license_LICENSE.jboss-logging.txt
/usr/share/package-licenses/mvn-netty/license_LICENSE.jsr166y.txt
/usr/share/package-licenses/mvn-netty/license_LICENSE.jzlib.txt
/usr/share/package-licenses/mvn-netty/license_LICENSE.log4j.txt
/usr/share/package-licenses/mvn-netty/license_LICENSE.protobuf.txt
/usr/share/package-licenses/mvn-netty/license_LICENSE.slf4j.txt
/usr/share/package-licenses/mvn-netty/license_LICENSE.webbit.txt
