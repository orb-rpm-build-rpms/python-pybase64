Name:           python-pybase64
Version:        1.5.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Fast Base64 encoding/decoding

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/mayeut/pybase64
Source:         %{pypi_source pybase64}

BuildRequires:  python3-devel
BuildRequires:  gcc
# pybase64 builds a bundled C base64 library via cmake from setup.py; without
# it the C extension is silently skipped, leaving an empty debugsource %files.
BuildRequires:  cmake


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pybase64' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pybase64
Summary:        %{summary}

%description -n python3-pybase64 %_description


%prep
%autosetup -p1 -n pybase64-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l pybase64


%check
%pyproject_check_import


%files -n python3-pybase64 -f %{pyproject_files}
%{_bindir}/pybase64


%changelog
%autochangelog
