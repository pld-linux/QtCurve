Summary:	A free and corrected port of Redhats gtk/qt theme
Summary(pl):	Wolna i poprawiona wersja tematu gtk/qt zrobionego przez Redhata
Name:		QtCurve
Version:	0.07
Release:	2
License:	GPL
Group:		Themes
# from		http://www.kde-look.org/content/download.php?content=5065
# redirected to	http://www.kde-look.org/content/files/5065-%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.kde-look.org/content/show.php?content=5065
BuildRequires:	qt >= 3.1
BuildRequires:	kdebase >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free and corrected port of Redhat's gtk/qt theme, made by Craig
Drummond <Craig.Drummond@lycos.co.uk>.

%description -l pl
Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata,
autorstwa Craiga Drummonda <Craig.Drummond@lycos.co.uk>.

%package -n kde-style-bluecurve
Summary:	A free and corrected port of Redhat's gtk/qt theme
Summary(pl):	Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata
Group:		Themes
Requires:	kdebase >= 3.1
Obsoletes:	kde-theme-bluecurve

%description -n kde-style-bluecurve
A free and corrected port of Redhat's gtk/qt theme, made by Craig
Drummond <Craig.Drummond@lycos.co.uk>. KDE version.

%description -n kde-style-bluecurve -l pl
Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata,
autorstwa Craiga Drummonda <Craig.Drummond@lycos.co.uk>. Wersja pod
KDE.

%package -n gtk-theme-bluecurve
Summary:        A free and corrected port of Redhat's gtk/qt theme
Summary(pl):    Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata
Group:          Themes
Requires:       gtk+ 
Requires:       theme-bluecurve-common

%description -n gtk-theme-bluecurve
A free and corrected port of Redhat's gtk/qt theme, made by Craig
Drummond <Craig.Drummond@lycos.co.uk>. gtk version.

%description -n gtk-theme-bluecurve -l pl
Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata,
autorstwa Craiga Drummonda <Craig.Drummond@lycos.co.uk>. Wersja pod
gtk.

%package -n gtk2-theme-bluecurve
Summary:        A free and corrected port of Redhat's gtk/qt theme
Summary(pl):    Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata
Group:          Themes
Requires:       gtk+
Requires:       theme-bluecurve-common

%description -n gtk2-theme-bluecurve
A free and corrected port of Redhat's gtk/qt theme, made by Craig
Drummond <Craig.Drummond@lycos.co.uk>. gtk2 version.

%description  -n gtk2-theme-bluecurve -l pl
Darmowa i poprawiona wersja motywu gtk/qt zrobionego przez Redhata,
autorstwa Craiga Drummonda <Craig.Drummond@lycos.co.uk>. Wersja pod
gtk2.

%package -n theme-bluecurve-common
Summary:        A free and corrected port of Redhats gtk/qt theme - common
Summary(pl):    Wolna i poprawiona wersja tematu gtk/qt zrobionego przez Redhata - common
Group:          Themes

%description -n theme-bluecurve-common
A free and corrected port of Redhats gtk/qt theme, made by Craig 
Drummond (Craig.Drummond@lycos.co.uk) Documentation and common 
files package.

%description  -n theme-bluecurve-common -l pl
Wolna i poprawiona wersja tematu gtk/qt zrobionego przez Redhata, 
autorstwa Craig Drummond (Craig.Drummond@lycos.co.uk) Pakiet z 
dokumentacja i plikami wspó³dzielonymi.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-style-bluecurve
%defattr(644,root,root,755)
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/qtcurve.themerc

%files -n gtk-theme-bluecurve
%defattr(644,root,root,755)
%{_libdir}/gtk/themes/engines/*.la
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*.so
%{_datadir}/themes/QtCurve/gtk

%files -n gtk2-theme-bluecurve
%defattr(644,root,root,755)
%{_libdir}/gtk-2.0/*/*/*.la
%attr(755,root,root) %{_libdir}/gtk-2.0/*/*/*.so
%{_datadir}/themes/QtCurve/gtk-2.0

%files -n theme-bluecurve-common
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%dir %{_datadir}/themes/QtCurve 
