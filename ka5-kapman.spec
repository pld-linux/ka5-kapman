%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kapman
Summary:	Kapman
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	742d18fec5eaadc3d19d18d5dbb7bc96
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kapman is a clone of the well known game Pac-Man.

You must run through the maze to eat all pills without being captured
by a ghost. By eating an energizer, Kapman gets the ability to eat
ghosts for a few seconds. When a stage is cleared of pills and
energizer the player is taken to the next stage with slightly
increased game speed.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kapman
%{_desktopdir}/org.kde.kapman.desktop
%{_iconsdir}/hicolor/128x128/apps/kapman.png
%{_iconsdir}/hicolor/16x16/apps/kapman.png
%{_iconsdir}/hicolor/22x22/apps/kapman.png
%{_iconsdir}/hicolor/32x32/apps/kapman.png
%{_iconsdir}/hicolor/48x48/apps/kapman.png
%{_iconsdir}/hicolor/64x64/apps/kapman.png
%{_datadir}/kapman
%dir %{_datadir}/kxmlgui5/kapman
%{_datadir}/kxmlgui5/kapman/kapmanui.rc
%{_datadir}/metainfo/org.kde.kapman.appdata.xml
%{_datadir}/sounds/kapman
