Summary:	GNUsound - a multitrack sound editor for GNOME
Summary(pl):	GNUsound - wielo�cie�kowy edytor d�wi�ku dla GNOME
Name:		gnusound
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	ftp://ftp.gnu.org/gnu/gnusound/%{name}-%{version}.tar.bz2
# Source0-md5:	43eef7373be32b5ec523f82dac5ba7bb
URL:		http://www.gnu.org/software/gnusound/
BuildRequires:	alsa-lib-devel >= 1.0.2
BuildRequires:	audiofile-devel >= 0.2.3
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.94
BuildRequires:	lame-libs-devel
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libogg-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel >= 1.0.4
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUsound is a multitrack sound editor for GNOME. It reads and writes
many audio formats such as WAV, MP3 and FLAC through its modular
system of file format drivers and can also extract the audio from
video formats like MPG, WMV and AVI through the FFmpeg file format
driver. It can use either OSS, ALSA or JACK for recording and playback
and interfaces with the LADSPA plugin system to provide a wide range
of high-quality audio processing plugins including filters,
compressors and delay effects.

The most important feature of GNUsound, however, is to stay out of
your way. This feature is not so easily expressed by a laundry list of
acronyms, so you'll just have to try it and see for yourself.

%description -l pl
GNUsound to wielo�cie�kowy edytor d�wi�ku dla GNOME. Czyta i zapisuje
wiele format�w d�wi�kowych, takich jak WAV, MP3 i FLAC poprzez
modularny system sterownik�w format�w plik�w; mo�e tak�e wydobywa�
d�wi�k z format�w video, takich jak MPG, WMV czy AVI poprzez sterownik
formatu plik�w FFmpeg. Mo�e tak�e u�ywa� sterownik�w OSS, ALSA albo
JACK do nagrywania i odtwarzania; wsp�pracuje z systemem wtyczek
LADSPA w celu dostarczenia szerokiej gamy wtyczek do przetwarzania
d�wi�ku wysokiej jako�ci, takich jak filtry, kompresory i efekty
op�niaj�ce.

Najwa�niejsz� cech� edytora GNUsound jest jednak to, �e nie stoi nam
na drodze. Ta cecha nie mo�e by� �atwo wyra�ona list� akronim�w, wi�c
trzeba to sprawdzi� samemu.

%prep
%setup -q

%build
%configure \
	--with-libsamplerate \
	--with-gnome2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_desktopdir} \
	owner_user=`id -nu` \
	owner_group=`id -ng`

# man page
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install doc/C/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES NOTES README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/%{name}*
