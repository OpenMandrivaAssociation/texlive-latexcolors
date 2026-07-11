%global tl_name latexcolors
%global tl_revision 49888

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1a
Release:	%{tl_revision}.1
Summary:	Use color definitions from latexcolor.com
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latexcolors
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcolors.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcolors.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcolors.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Built on top of the xcolor package, the latexcolors package defines the
set of colors shown on latexcolor.com for use in documents typeset with
LaTeX & friends.

