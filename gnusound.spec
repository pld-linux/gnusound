Summary:	GNUsound is a multitrack sound editor for GNOME
Name:		gnusound
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
URL:		http://www.gnu.org/software/gnusound/
Source0:	ftp://ftp.gnu.org/gnu/gnusound/%{name}-%{version}.tar.bz2
# Source0-md5:	43eef7373be32b5ec523f82dac5ba7bb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	alsa-lib-devel >= 1.0.2
BuildRequires:	jack-audio-connection-kit-devel >= 0.94
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	flac-devel
BuildRequires:	libsndfile-devel >= 1.0.4
BuildRequires:	lame
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRequires:	pkgconfig
BuildRequires:	ladspa
BuildRequires:	audiofile >= 0.2.3
BuildRequires:	zlib-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libxml2-devel
BuildRequires:	ORBit2-devel
BuildRequires:	libgnomeui-devel

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

%prep
%setup -q

%build
%configure \
	--with-libsamplerate \
	--with-gnome2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	owner_user=`whoami` \
	owner_group=users \
	install

# man page
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install doc/C/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL LICENSE NOTES README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/gnome/help
%{_applnkdir}/*
%{_mandir}/man1/%{name}*
