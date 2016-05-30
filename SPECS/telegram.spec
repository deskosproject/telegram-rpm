Name:           telegram
Version:        0.9.48
Release:        1%{?dist}
Summary:        Telegram is a messaging app with a focus on speed and security, it’s super fast, simple and free. You can use Telegram on all your devices at the same time.

Group:          Internet/Messaging
License:        GPLv3
URL:            https://telegram.org/

Source0:        https://updates.tdesktop.com/tlinux32/tsetup32.%version.tar.xz
Source1:        https://updates.tdesktop.com/tlinux/tsetup.%version.tar.xz
Source2:        telegram.png
Source3:        telegram.desktop

BuildRequires:  desktop-file-utils

%description
Telegram is a messaging app with a focus on speed and security, it’s super
fast, simple and free. You can use Telegram on all your devices at the same
time — your messages sync seamlessly across any of your phones, tablets or
computers.

With Telegram, you can send messages, photos, videos and files of any type
(doc, zip, mp3, etc), as well as create groups for up to 200 people. You can
write to your phone contacts and find people by their usernames. As a result,
Telegram is like SMS and email combined — and can take care of all your
personal or business messaging needs.

%prep
%ifarch %ix86
%setup -b0 -q -n Telegram
%endif

%ifarch x86_64 amd64
%setup -b1 -q -n Telegram
%endif

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_bindir}

cp -arf ./Telegram %{buildroot}%{_datadir}/%{name}/telegram
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/

ln -s %{_datadir}/%{name}/telegram %{buildroot}%{_bindir}/telegram

cp %{SOURCE3} %{buildroot}%{_datadir}/%{name}.desktop

desktop-file-install \
	--add-category="Network" \
	--delete-original \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/%{name}.desktop

%files
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/telegram
%{_datadir}/applications/telegram.desktop
%{_datadir}/pixmaps/telegram.png
%{_bindir}/telegram

%changelog
* Mon May 30 2016 Ricardo Arguello <rarguello@deskosproject.org - 0.9.48-1
- Initial DeskOS release.
