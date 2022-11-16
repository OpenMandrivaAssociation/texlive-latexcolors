Name:		texlive-latexcolors
Version:	49888
Release:	1
Summary:	Use color definitions from latexcolor.com
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latexcolors
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcolors.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcolors.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcolors.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Built on top of the xcolor package, the latexcolors package
defines the set of colors shown on latexcolor.com for use in
documents typeset with LaTeX & friends.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/latexcolors
%{_texmfdistdir}/tex/latex/latexcolors
%doc %{_texmfdistdir}/doc/latex/latexcolors

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
