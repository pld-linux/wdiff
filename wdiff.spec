Summary:	Word-based diff front end
Name:		wdiff
Version:	1.2.2
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/wdiff/%{name}-%{version}.tar.gz
# Source0-md5:	1c6ddd1f3106139ff9fe00e934df715f
URL:		http://www.gnu.org/software/wdiff/wdiff.html
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNU wdiff program is a front end to diff for comparing files on a
word per word basis. A word is anything between whitespace. This is
useful for comparing two texts in which a few words have been changed
and for which paragraphs have been refilled. It works by creating two
temporary files, one word per line, and then executes diff on these
files. It collects the diff output and uses it to produce a nicer
display of word differences between the original files.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/wdiff
%{_infodir}/wdiff.info*
%{_mandir}/man1/wdiff.1*
