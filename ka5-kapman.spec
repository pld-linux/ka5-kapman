#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.04.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kapman
Summary:	Kapman
Name:		ka5-%{kaname}
Version:	23.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9128ee5bdafde44ba003450e48a16c8c
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
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
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

%description -l pl.UTF-8
Kapman jest klonem dobrze znanej gry Pac-Man.

Musisz przemieszczać się przez labirynt, połykać pigułki i unikać duchów.
Zjadając energetyka, Kapman otrzymuje moc zjadania duchów, która trwa
kilka sekund. Gdy plansza zostanie wyczyszczona z pigułek i energetyka,
gracz jest przenoszony na następny poziom z nieco przyspieszoną rozgrywką.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


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
%{_datadir}/metainfo/org.kde.kapman.appdata.xml
%{_datadir}/sounds/kapman
