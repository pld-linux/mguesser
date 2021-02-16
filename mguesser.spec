Summary:	Guess character set and language of a text file
Name:		mguesser
Version:	0.4
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://www.mnogosearch.org/guesser/%{name}-%{version}.tar.gz
# Source0-md5:	ebd99d140136a2167cf465641a666519
URL:		http://www.mnogosearch.org/guesser/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mguesser is a standalone part of libmnogosearch (a core of mnogo
search engine http://www.mnogosearch.org) which allows to guess
character set and language of a text file.

mguesser is implemented using "N-Gram-Based Text Categorization"
technique which is implemented in TextCat language guesser written in
Perl (http://www.let.rug.nl/~vannoord/TextCat/). mguesser is
significantly faster than TextCat especially on large texts.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} -DUDM_GUESSER_STANDALONE -DLMDIR=\\\"%{_datadir}/mguesser/maps\\\" -DMGUESSER_VERSION=\\\"%{version}\\\""

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/mguesser}
cp -p mguesser $RPM_BUILD_ROOT%{_bindir}
cp -pr maps $RPM_BUILD_ROOT%{_datadir}/mguesser

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/mguesser
%{_datadir}/mguesser
