Summary:	GNUsound - a multitrack sound editor for GNOME
Summary(pl.UTF-8):	GNUsound - wielościeżkowy edytor dźwięku dla GNOME
Name:		gnusound
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://ftp.gnu.org/gnu/gnusound/%{name}-%{version}.tar.bz2
# Source0-md5:	43eef7373be32b5ec523f82dac5ba7bb
Source1:	%{name}.desktop
Patch0:		%{name}-Makefiles.patch
URL:		http://www.gnu.org/software/gnusound/
BuildRequires:	alsa-lib-devel >= 1.0.2
BuildRequires:	audiofile-devel >= 0.2.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ffmpeg-devel >= 0.4.9
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

%description -l pl.UTF-8
GNUsound to wielościeżkowy edytor dźwięku dla GNOME. Czyta i zapisuje
wiele formatów dźwiękowych, takich jak WAV, MP3 i FLAC poprzez
modularny system sterowników formatów plików; może także wydobywać
dźwięk z formatów video, takich jak MPG, WMV czy AVI poprzez sterownik
formatu plików FFmpeg. Może także używać sterowników OSS, ALSA albo
JACK do nagrywania i odtwarzania; współpracuje z systemem wtyczek
LADSPA w celu dostarczenia szerokiej gamy wtyczek do przetwarzania
dźwięku wysokiej jakości, takich jak filtry, kompresory i efekty
opóźniające.

Najważniejszą cechą edytora GNUsound jest jednak to, że nie stoi nam
na drodze. Ta cecha nie może być łatwo wyrażona listą akronimów, więc
trzeba to sprawdzić samemu.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub config
%{__aclocal} -I config
%{__autoconf} -I config
%configure \
	--with-libsamplerate \
	--with-gnome2

%{__make} CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_desktopdir}

install -D doc/C/gnusound.1 $RPM_BUILD_ROOT%{_mandir}/man1/gnusound.1
install -D gui/logo.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/gnusound.xpm
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/gnusound.desktop

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES NOTES README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/gnusound.xpm
%{_mandir}/man1/%{name}*
