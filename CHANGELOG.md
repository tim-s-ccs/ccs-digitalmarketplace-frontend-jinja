# Digital Marketplace Frontend Jinja

Records breaking changes from major version bumps.

## 1.3.0rc1

Upgrade Flask to v2.3

## 1.2.0

Allow for use with all currently maintained Python versions:
- 3.9
- 3.10
- 3.11

Note, because ccs-digitalmarketplace-utils does not support 3.12 yet, neither can we.

## 1.1.0

Upgrade Flask to v2 and, therefore, Jinja to v3

Upgrade GOV.UK Frontend Jinja to v2.8 (Node 4.8)

## 1.0.0

🆕 New features:

  Add macros for the following components:

  | Component name            | Macro name                                  |
  |---------------------------|---------------------------------------------|
  | Alert                     | `digitalmarketplaceAlert`                   |
  | Attachment                | `digitalmarketplaceAttachment`              |
  | Banner                    | `digitalmarketplaceBanner`                  |
  | Character Count From Form | `digitalmarketplaceCharacterCountFromForm`  |
  | Checkboxes From Form      | `digitalmarketplaceCheckboxesFromForm`      |
  | Cookie Banner             | `digitalmarketplaceCookieBanner`            |
  | Documents                 | `digitalmarketplaceDocuments`               |
  | Footer                    | `digitalmarketplaceFooter`                  |
  | Header                    | `digitalmarketplaceHeader`                  |
  | Input From Form           | `digitalmarketplaceInputFromForm`           |
  | List Input                | `digitalmarketplaceListInput`               |
  | New Framework Banner      | `digitalmarketplaceNewFrameworkBanner`      |
  | Option Select             | `digitalmarketplaceOptionSelect`            |
  | Previous Next Pagination  | `digitalmarketplacePreviousNextPagination`  |
  | Question                  | `digitalmarketplaceQuestion`                |
  | Radios From Form          | `digitalmarketplaceRadiosFromForm`          |
  | Search Box                | `digitalmarketplaceSearchBox`               |
  | Select Country From Form  | `digitalmarketplaceSelectCountryFromForm`   |
  | Summary Content           | `digitalmarketplaceSummaryContent`          |
  | Temporary Message         | `digitalmarketplaceTemporaryMessage`        |

  Add the following layouts:

  - `layouts/_custom_dimensions.html`
  - `layouts/_site_verification.html`

  Add the following error page templates:

  - `errors/400.html`
  - `errors/403.html`
  - `errors/404.html`
  - `errors/410.html`
  - `errors/500.html`
