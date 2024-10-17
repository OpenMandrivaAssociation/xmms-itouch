Name:		xmms-itouch
Version:	0.1.2
Release:	%mkrel 11
Epoch:		0
Summary:	XMMS iTouch keyboard control plugin
License:	GPL
Group:		Sound
URL:		https://www.saunalahti.fi/~syrjala/xmms-itouch/
Source0:	http://www.saunalahti.fi/~syrjala/xmms-itouch/%{name}-%{version}.tar.bz2
Source1:	http://www.saunalahti.fi/~syrjala/xmms-itouch/%{name}.config
Requires:	xmms
BuildRequires:	xmms-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-release-root

%description
With this XMMS plugin you can take advantage of the multimedia (playback and
volume control) keys on your Logitech iTouch keyboard. When the plugin is
used you can use the keys regardless of the current input focus. The plugin
won't work if some other application (eg. xscreensaver) has grabbed the
keyboard.
	
%prep
%setup -q
%{__cp} -a %{SOURCE1} %{name}.config

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} %{buildroot}%{_libdir}/xmms/General/libitouch.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL README
%{_datadir}/xmms/xmms-itouch.config
%attr(0755,root,root) %{_libdir}/xmms/General/libitouch.so
