#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 81e1eeb
#
Name     : R-renv
Version  : 1.0.7
Release  : 11
URL      : https://cran.r-project.org/src/contrib/renv_1.0.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/renv_1.0.7.tar.gz
Summary  : Project Environments
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
and manage project-local R libraries, save the state of these libraries to
    a 'lockfile', and later restore your library as required. Together, these
    tools can help make your projects more isolated, portable, and reproducible.

%prep
%setup -q -n renv
pushd ..
cp -a renv buildavx2
popd
pushd ..
cp -a renv buildavx512
popd
pushd ..
cp -a renv buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1712943796

%install
export SOURCE_DATE_EPOCH=1712943796
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/renv/DESCRIPTION
/usr/lib64/R/library/renv/INDEX
/usr/lib64/R/library/renv/LICENSE
/usr/lib64/R/library/renv/Meta/Rd.rds
/usr/lib64/R/library/renv/Meta/features.rds
/usr/lib64/R/library/renv/Meta/hsearch.rds
/usr/lib64/R/library/renv/Meta/links.rds
/usr/lib64/R/library/renv/Meta/nsInfo.rds
/usr/lib64/R/library/renv/Meta/package.rds
/usr/lib64/R/library/renv/Meta/vignette.rds
/usr/lib64/R/library/renv/NAMESPACE
/usr/lib64/R/library/renv/NEWS.md
/usr/lib64/R/library/renv/R/renv
/usr/lib64/R/library/renv/R/renv.rdb
/usr/lib64/R/library/renv/R/renv.rdx
/usr/lib64/R/library/renv/bin/renv
/usr/lib64/R/library/renv/bin/renv.bat
/usr/lib64/R/library/renv/config.yml
/usr/lib64/R/library/renv/doc/ci.R
/usr/lib64/R/library/renv/doc/ci.Rmd
/usr/lib64/R/library/renv/doc/ci.html
/usr/lib64/R/library/renv/doc/docker.R
/usr/lib64/R/library/renv/doc/docker.Rmd
/usr/lib64/R/library/renv/doc/docker.html
/usr/lib64/R/library/renv/doc/faq.R
/usr/lib64/R/library/renv/doc/faq.Rmd
/usr/lib64/R/library/renv/doc/faq.html
/usr/lib64/R/library/renv/doc/index.html
/usr/lib64/R/library/renv/doc/package-install.R
/usr/lib64/R/library/renv/doc/package-install.Rmd
/usr/lib64/R/library/renv/doc/package-install.html
/usr/lib64/R/library/renv/doc/package-sources.R
/usr/lib64/R/library/renv/doc/package-sources.Rmd
/usr/lib64/R/library/renv/doc/package-sources.html
/usr/lib64/R/library/renv/doc/packages.R
/usr/lib64/R/library/renv/doc/packages.Rmd
/usr/lib64/R/library/renv/doc/packages.html
/usr/lib64/R/library/renv/doc/packrat.R
/usr/lib64/R/library/renv/doc/packrat.Rmd
/usr/lib64/R/library/renv/doc/packrat.html
/usr/lib64/R/library/renv/doc/profiles.R
/usr/lib64/R/library/renv/doc/profiles.Rmd
/usr/lib64/R/library/renv/doc/profiles.html
/usr/lib64/R/library/renv/doc/python.R
/usr/lib64/R/library/renv/doc/python.Rmd
/usr/lib64/R/library/renv/doc/python.html
/usr/lib64/R/library/renv/doc/renv.R
/usr/lib64/R/library/renv/doc/renv.Rmd
/usr/lib64/R/library/renv/doc/renv.html
/usr/lib64/R/library/renv/doc/rsconnect.R
/usr/lib64/R/library/renv/doc/rsconnect.Rmd
/usr/lib64/R/library/renv/doc/rsconnect.html
/usr/lib64/R/library/renv/help/AnIndex
/usr/lib64/R/library/renv/help/aliases.rds
/usr/lib64/R/library/renv/help/figures/logo.svg
/usr/lib64/R/library/renv/help/paths.rds
/usr/lib64/R/library/renv/help/renv.rdb
/usr/lib64/R/library/renv/help/renv.rdx
/usr/lib64/R/library/renv/html/00Index.html
/usr/lib64/R/library/renv/html/R.css
/usr/lib64/R/library/renv/repos/src/contrib/PACKAGES
/usr/lib64/R/library/renv/repos/src/contrib/PACKAGES.gz
/usr/lib64/R/library/renv/repos/src/contrib/PACKAGES.rds
/usr/lib64/R/library/renv/repos/src/contrib/renv_1.0.7.tar.gz
/usr/lib64/R/library/renv/resources/WELCOME
/usr/lib64/R/library/renv/resources/activate.R
/usr/lib64/R/library/renv/resources/scripts-git-askpass.cmd
/usr/lib64/R/library/renv/resources/scripts-git-askpass.sh
/usr/lib64/R/library/renv/resources/vendor/renv.R
/usr/lib64/R/library/renv/resources/watchdog-process.R
/usr/lib64/R/library/renv/rstudio/addins.dcf
/usr/lib64/R/library/renv/tests/testthat.R
/usr/lib64/R/library/renv/tests/testthat/_snaps/activate.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/bioconductor.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/bootstrap.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/caution.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/dependencies.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/dots.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/init.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/install.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/load.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/lockfile-read.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/preflight.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/repair.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/snapshot.md
/usr/lib64/R/library/renv/tests/testthat/_snaps/status.md
/usr/lib64/R/library/renv/tests/testthat/helper-aaa.R
/usr/lib64/R/library/renv/tests/testthat/helper-interactive.R
/usr/lib64/R/library/renv/tests/testthat/helper-scope.R
/usr/lib64/R/library/renv/tests/testthat/helper-setup.R
/usr/lib64/R/library/renv/tests/testthat/helper-skip.R
/usr/lib64/R/library/renv/tests/testthat/helper-slow.R
/usr/lib64/R/library/renv/tests/testthat/helper-snapshot.R
/usr/lib64/R/library/renv/tests/testthat/helper-testthat.R
/usr/lib64/R/library/renv/tests/testthat/helper-watchdog.R
/usr/lib64/R/library/renv/tests/testthat/helper-zzz.R
/usr/lib64/R/library/renv/tests/testthat/local/skeleton/skeleton_1.0.0.tar.gz
/usr/lib64/R/library/renv/tests/testthat/local/skeleton/skeleton_1.0.1.tar.gz
/usr/lib64/R/library/renv/tests/testthat/packages/bread/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/breakfast/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/brunch/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/egg/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/halloween/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/jamie/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/kevin/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/oatmeal/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/packrat/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/packrat/README
/usr/lib64/R/library/renv/tests/testthat/packages/phone/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/renv/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/toast/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/unixonly/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/packages/windowsonly/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/resources/DESCRIPTION
/usr/lib64/R/library/renv/tests/testthat/resources/bioconductor.lock
/usr/lib64/R/library/renv/tests/testthat/resources/box.R
/usr/lib64/R/library/renv/tests/testthat/resources/bslib.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/chunk-errors.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/chunk-eval.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/chunk-yaml.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/code.R
/usr/lib64/R/library/renv/tests/testthat/resources/empty-chunk.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/empty-label.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/eval.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/evil.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/glue.R
/usr/lib64/R/library/renv/tests/testthat/resources/ignore.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/import.R
/usr/lib64/R/library/renv/tests/testthat/resources/inline-chunks.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/knitr-reused-chunks.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/learnr-exercise.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/magrittr.R
/usr/lib64/R/library/renv/tests/testthat/resources/manifest.json
/usr/lib64/R/library/renv/tests/testthat/resources/modules.R
/usr/lib64/R/library/renv/tests/testthat/resources/multiple-output-formats.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/notebook.ipynb
/usr/lib64/R/library/renv/tests/testthat/resources/pacman.R
/usr/lib64/R/library/renv/tests/testthat/resources/params.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/parsnip.R
/usr/lib64/R/library/renv/tests/testthat/resources/properties.txt
/usr/lib64/R/library/renv/tests/testthat/resources/quarto-empty.qmd
/usr/lib64/R/library/renv/tests/testthat/resources/quarto-r-chunks.qmd
/usr/lib64/R/library/renv/tests/testthat/resources/rmd-base-format.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/shiny-prerendered.Rmd
/usr/lib64/R/library/renv/tests/testthat/resources/targets.R
/usr/lib64/R/library/renv/tests/testthat/resources/utility
/usr/lib64/R/library/renv/tests/testthat/resources/yaml-chunks.Rmd
/usr/lib64/R/library/renv/tests/testthat/test-acls.R
/usr/lib64/R/library/renv/tests/testthat/test-actions.R
/usr/lib64/R/library/renv/tests/testthat/test-activate.R
/usr/lib64/R/library/renv/tests/testthat/test-archive.R
/usr/lib64/R/library/renv/tests/testthat/test-authentication.R
/usr/lib64/R/library/renv/tests/testthat/test-autoload.R
/usr/lib64/R/library/renv/tests/testthat/test-available-packages.R
/usr/lib64/R/library/renv/tests/testthat/test-base64.R
/usr/lib64/R/library/renv/tests/testthat/test-bind.R
/usr/lib64/R/library/renv/tests/testthat/test-binding.R
/usr/lib64/R/library/renv/tests/testthat/test-bioconductor.R
/usr/lib64/R/library/renv/tests/testthat/test-bootstrap.R
/usr/lib64/R/library/renv/tests/testthat/test-cache.R
/usr/lib64/R/library/renv/tests/testthat/test-call.R
/usr/lib64/R/library/renv/tests/testthat/test-caution.R
/usr/lib64/R/library/renv/tests/testthat/test-cellar.R
/usr/lib64/R/library/renv/tests/testthat/test-checkout.R
/usr/lib64/R/library/renv/tests/testthat/test-clean.R
/usr/lib64/R/library/renv/tests/testthat/test-cleanse.R
/usr/lib64/R/library/renv/tests/testthat/test-config.R
/usr/lib64/R/library/renv/tests/testthat/test-consent.R
/usr/lib64/R/library/renv/tests/testthat/test-dcf.R
/usr/lib64/R/library/renv/tests/testthat/test-deactivate.R
/usr/lib64/R/library/renv/tests/testthat/test-defer.R
/usr/lib64/R/library/renv/tests/testthat/test-dependencies.R
/usr/lib64/R/library/renv/tests/testthat/test-description.R
/usr/lib64/R/library/renv/tests/testthat/test-dots.R
/usr/lib64/R/library/renv/tests/testthat/test-download.R
/usr/lib64/R/library/renv/tests/testthat/test-dynamic.R
/usr/lib64/R/library/renv/tests/testthat/test-envvar.R
/usr/lib64/R/library/renv/tests/testthat/test-envvars.R
/usr/lib64/R/library/renv/tests/testthat/test-errors.R
/usr/lib64/R/library/renv/tests/testthat/test-expr.R
/usr/lib64/R/library/renv/tests/testthat/test-filebacked.R
/usr/lib64/R/library/renv/tests/testthat/test-files.R
/usr/lib64/R/library/renv/tests/testthat/test-hash.R
/usr/lib64/R/library/renv/tests/testthat/test-history.R
/usr/lib64/R/library/renv/tests/testthat/test-http.R
/usr/lib64/R/library/renv/tests/testthat/test-hydrate.R
/usr/lib64/R/library/renv/tests/testthat/test-id.R
/usr/lib64/R/library/renv/tests/testthat/test-index.R
/usr/lib64/R/library/renv/tests/testthat/test-infrastructure.R
/usr/lib64/R/library/renv/tests/testthat/test-init.R
/usr/lib64/R/library/renv/tests/testthat/test-install.R
/usr/lib64/R/library/renv/tests/testthat/test-internal.R
/usr/lib64/R/library/renv/tests/testthat/test-json.R
/usr/lib64/R/library/renv/tests/testthat/test-load.R
/usr/lib64/R/library/renv/tests/testthat/test-lock.R
/usr/lib64/R/library/renv/tests/testthat/test-lockfile-read.R
/usr/lib64/R/library/renv/tests/testthat/test-lockfile.R
/usr/lib64/R/library/renv/tests/testthat/test-memoize.R
/usr/lib64/R/library/renv/tests/testthat/test-metadata.R
/usr/lib64/R/library/renv/tests/testthat/test-migrate.R
/usr/lib64/R/library/renv/tests/testthat/test-miscellaneous.R
/usr/lib64/R/library/renv/tests/testthat/test-modify.R
/usr/lib64/R/library/renv/tests/testthat/test-mran.R
/usr/lib64/R/library/renv/tests/testthat/test-once.R
/usr/lib64/R/library/renv/tests/testthat/test-packages.R
/usr/lib64/R/library/renv/tests/testthat/test-parse.R
/usr/lib64/R/library/renv/tests/testthat/test-patches.R
/usr/lib64/R/library/renv/tests/testthat/test-path.R
/usr/lib64/R/library/renv/tests/testthat/test-paths.R
/usr/lib64/R/library/renv/tests/testthat/test-platform.R
/usr/lib64/R/library/renv/tests/testthat/test-ppm.R
/usr/lib64/R/library/renv/tests/testthat/test-preflight.R
/usr/lib64/R/library/renv/tests/testthat/test-profile.R
/usr/lib64/R/library/renv/tests/testthat/test-profiles.R
/usr/lib64/R/library/renv/tests/testthat/test-properties.R
/usr/lib64/R/library/renv/tests/testthat/test-purge.R
/usr/lib64/R/library/renv/tests/testthat/test-python.R
/usr/lib64/R/library/renv/tests/testthat/test-r.R
/usr/lib64/R/library/renv/tests/testthat/test-rebuild.R
/usr/lib64/R/library/renv/tests/testthat/test-record.R
/usr/lib64/R/library/renv/tests/testthat/test-records.R
/usr/lib64/R/library/renv/tests/testthat/test-rehash.R
/usr/lib64/R/library/renv/tests/testthat/test-reload.R
/usr/lib64/R/library/renv/tests/testthat/test-remotes.R
/usr/lib64/R/library/renv/tests/testthat/test-renvignore.R
/usr/lib64/R/library/renv/tests/testthat/test-repair.R
/usr/lib64/R/library/renv/tests/testthat/test-repos.R
/usr/lib64/R/library/renv/tests/testthat/test-restore.R
/usr/lib64/R/library/renv/tests/testthat/test-retrieve.R
/usr/lib64/R/library/renv/tests/testthat/test-rmd.R
/usr/lib64/R/library/renv/tests/testthat/test-sandbox.R
/usr/lib64/R/library/renv/tests/testthat/test-scaffold.R
/usr/lib64/R/library/renv/tests/testthat/test-scope.R
/usr/lib64/R/library/renv/tests/testthat/test-settings.R
/usr/lib64/R/library/renv/tests/testthat/test-snapshot.R
/usr/lib64/R/library/renv/tests/testthat/test-socket.R
/usr/lib64/R/library/renv/tests/testthat/test-status.R
/usr/lib64/R/library/renv/tests/testthat/test-system.R
/usr/lib64/R/library/renv/tests/testthat/test-truthy.R
/usr/lib64/R/library/renv/tests/testthat/test-update.R
/usr/lib64/R/library/renv/tests/testthat/test-upgrade.R
/usr/lib64/R/library/renv/tests/testthat/test-url.R
/usr/lib64/R/library/renv/tests/testthat/test-use.R
/usr/lib64/R/library/renv/tests/testthat/test-utils.R
/usr/lib64/R/library/renv/tests/testthat/test-vendor.R
/usr/lib64/R/library/renv/tests/testthat/test-version.R
/usr/lib64/R/library/renv/tests/testthat/test-watchdog.R
