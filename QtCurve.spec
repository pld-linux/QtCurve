#
# Conditional build:
%bcond_without gtk	# do not build gtk+(2) styles
#
Summary:	A free and corrected port of Redhats gtk/qt theme
Summary(pl):	Darmowa i poprawiona wersja tematu gtk/qt zrobionego przez Redhata
Name:		QtCurve
Version:	0.19
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.cpdrummond.freeuk.com/%{name}-%{version}.tar.gz
# Source0-md5:	b42974ade8866c1b00808af9f0e47d61
URL:		http://www.kde-look.org/content/show.php?content=5065
BuildRequires:  automake
BuildRequires:	kdelibs-devel >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free and corrected port of Redhat's gtk/qt theme.

%description -l pl
Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata.

%package -n kde-style-QtCurve
Summary:	A free and corrected port of Redhat's gtk/qt theme
Summary(pl):	Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata
Group:		Themes
Requires:	kdelibs >= 3.1

%description -n kde-style-QtCurve
A free and corrected port of Redhat's gtk/qt theme. KDE version.

%description -n kde-style-QtCurve -l pl
Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata.
Wersja pod KDE.

%package -n gtk-theme-QtCurve
Summary:	A free and corrected port of Redhat's gtk/qt theme
Summary(pl):	Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata
Group:		Themes
Requires:	gtk+
Requires:	theme-QtCurve-common = %{version}-%{release}

%description -n gtk-theme-QtCurve
A free and corrected port of Redhat's gtk/qt theme. gtk version.

%description -n gtk-theme-QtCurve -l pl
Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata.
Wersja pod gtk.

%package -n gtk2-theme-QtCurve
Summary:	A free and corrected port of Redhat's gtk/qt theme
Summary(pl):	Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata
Group:		Themes
Requires:	gtk+
Requires:	theme-QtCurve-common = %{version}-%{release}

%description -n gtk2-theme-QtCurve
A free and corrected port of Redhat's gtk/qt theme. gtk2 version.

%description -n gtk2-theme-QtCurve -l pl
Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata.
Wersja pod gtk2.

%package -n theme-QtCurve-common
Summary:	A free and corrected port of Redhats gtk/qt theme - common
Summary(pl):	Darmowa i poprawiona wersja tematu gtk/qt zrobionego przez Redhata - common
Group:		Themes
Obsoletes:	theme-bluecurve-common
Obsoletes:	gtk2-theme-bluecurve
Obsoletes:	gtk-theme-bluecurve
Obsoletes:	kde-style-bluecurve
Obsoletes:	kde-theme-bluecurve

%description -n theme-QtCurve-common
A free and corrected port of Redhats gtk/qt theme.
Documentation and common files package.

%description -n theme-QtCurve-common -l pl
Darmowa i poprawiona wersja tematu gtk/qt zrobionego przez Redhata.
Pakiet z dokumentacja i plikami wspó³dzielonymi.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub admin

%{!?with_gtk:export "DO_NOT_COMPILE=gtk gtk2"}
##export UNSERMAKE=/usr/share/unsermake/unsermake
##%{__make} -f admin/Makefile.common cvs
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT{%{_libdir}/gtk/themes/engines,%{_libdir}/gtk-2.0/*/*}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-style-QtCurve
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_qtcurve_config.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_qtcurve_config.so
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/qtcurve*.themerc

%if %{with gtk}
%files -n gtk-theme-QtCurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*.so
%{_datadir}/themes/QtCurve*/gtk

%files -n gtk2-theme-QtCurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/*/*/*.so
%{_datadir}/themes/QtCurve*/gtk-2.0

%files -n theme-QtCurve-common
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%dir %{_datadir}/themes/QtCurve*
%endif
