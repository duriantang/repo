%global commit      79e81f94df4cdce27cc76872e54dbd4d66cc76b2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           dtkwidget
Version:        2.0.1
Release:        2%{?dist}
Summary:        Deepin tool kit widget modules
License:        GPLv3
URL:            https://github.com/linuxdeepin/dtkwidget
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-static
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)
Provides:       deepin-tool-kit%{_isa} = %{version}-%{release}
Obsoletes:      deepin-tool-kit%{_isa} < %{version}-%{release}

%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{name}-%{commit}
sed -i 's|lrelease|lrelease-qt5|g' tools/translate_generation.sh
sed -i 's|/lib|/libexec|' tools/svgc/svgc.pro

%build
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.*
%{_libexecdir}/dtk2/dtk-svgc
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/translations/

%files devel
%{_includedir}/libdtk-*/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 2.0.1-2
- Fix DAboutDialog icon not supporting hidpi

* Tue Oct 17 2017 mosquito <sensor.wen@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Thu Aug 24 2017 mosquito <sensor.wen@gmail.com> - 2.0.0-2
- Dont depend a specific version of Qt

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Sat Jul 29 2017 mosquito <sensor.wen@gmail.com> - 0.3.3-1
- Initial package build
