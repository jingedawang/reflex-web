import reflex as rx


def card(company: str, text: str) -> rx.Component:
    return rx.link(
        # Top-Left corner company logo
        rx.image(
            src=rx.color_mode_cond(
                light=f"/customers/light/{company}/{company}_top.svg",
                dark=f"/customers/dark/{company}/{company}_top.svg",
            ),
            alt=f"{company} logo",
            loading="lazy",
            class_name="absolute top-10 left-10 z-[2]",
        ),
        # Center company logo
        rx.image(
            rx.color_mode_cond(
                light=f"/customers/light/{company}/{company}_middle.svg",
                dark=f"/customers/dark/{company}/{company}_middle.svg",
            ),
            alt=f"{company} small logo",
            loading="lazy",
            class_name="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[2]",
        ),
        # Wave pattern
        rx.html(
            """<svg xmlns="http://www.w3.org/2000/svg" width="546" height="372" viewBox="0 0 546 372" fill="none">
              <path d="M312.215 179.166C316.027 200.785 301.591 221.402 279.971 225.214C258.352 229.026 237.735 214.59 233.923 192.971C230.111 171.351 244.547 150.734 266.166 146.922C287.786 143.11 308.403 157.546 312.215 179.166ZM280.058 225.707C301.95 221.847 316.568 200.971 312.707 179.079C308.847 157.187 287.971 142.57 266.08 146.43C244.188 150.29 229.57 171.166 233.43 193.057C237.291 214.949 258.167 229.567 280.058 225.707ZM325.456 167.001C335.987 195.934 321.069 227.925 292.136 238.456C263.203 248.987 231.211 234.069 220.68 205.136C210.15 176.203 225.067 144.211 254.001 133.68C282.934 123.15 314.925 138.067 325.456 167.001ZM292.307 238.926C321.499 228.301 336.551 196.022 325.926 166.829C315.301 137.637 283.022 122.585 253.829 133.21C224.637 143.836 209.585 176.114 220.21 205.307C230.836 234.499 263.114 249.551 292.307 238.926ZM335.206 150.193C355.019 184.511 343.261 228.392 308.944 248.205C274.626 268.019 230.745 256.261 210.932 221.943C191.118 187.626 202.876 143.744 237.194 123.931C271.511 104.118 315.393 115.876 335.206 150.193ZM309.194 248.638C343.751 228.687 355.591 184.5 335.639 149.943C315.688 115.387 271.501 103.547 236.944 123.498C202.387 143.449 190.547 187.637 210.499 222.193C230.45 256.75 274.637 268.59 309.194 248.638ZM340.289 129.664C371.44 166.788 366.598 222.137 329.473 253.289C292.348 284.44 236.999 279.598 205.848 242.473C174.696 205.348 179.539 149.999 216.664 118.848C253.788 87.6963 309.137 92.5387 340.289 129.664ZM329.794 253.672C367.131 222.343 372.001 166.678 340.672 129.342C309.343 92.0058 253.679 87.1358 216.342 118.465C179.006 149.794 174.136 205.458 205.465 242.794C236.794 280.13 292.458 285 329.794 253.672ZM339.758 106.591C383.652 143.422 389.377 208.863 352.546 252.757C315.714 296.651 250.273 302.377 206.379 265.545C162.485 228.714 156.76 163.273 193.591 119.379C230.423 75.485 295.864 69.7596 339.758 106.591ZM352.929 253.079C389.938 208.973 384.185 143.217 340.079 106.208C295.974 69.1991 230.217 74.952 193.208 119.058C156.199 163.163 161.952 228.919 206.058 265.928C250.163 302.937 315.92 297.184 352.929 253.079ZM332.944 82.3616C390.219 115.43 409.843 188.668 376.775 245.943C343.707 303.219 270.469 322.843 213.194 289.775C155.918 256.707 136.294 183.469 169.362 126.193C202.43 68.9176 275.668 49.2935 332.944 82.3616ZM377.208 246.193C410.414 188.678 390.708 115.135 333.194 81.9286C275.679 48.7224 202.135 68.4284 168.929 125.943C135.723 183.458 155.429 257.002 212.944 290.208C270.458 323.414 344.002 303.708 377.208 246.193ZM319.498 58.5049C389.95 84.147 426.274 162.046 400.632 232.497C374.99 302.949 297.091 339.274 226.64 313.631C156.189 287.989 119.864 210.09 145.506 139.639C171.148 69.1877 249.047 32.8627 319.498 58.5049ZM401.102 232.668C426.839 161.958 390.38 83.7716 319.669 58.035C248.959 32.2984 170.773 68.7572 145.036 139.468C119.299 210.179 155.758 288.365 226.469 314.101C297.18 339.838 375.366 303.379 401.102 232.668ZM299.42 36.6236C381.956 51.1769 437.067 129.883 422.513 212.419C407.96 294.955 329.254 350.066 246.718 335.513C164.182 320.959 109.071 242.253 123.624 159.717C138.178 77.1811 216.884 22.0702 299.42 36.6236ZM423.006 212.506C437.607 129.698 382.315 50.7324 299.507 36.1311C216.699 21.5299 137.733 76.8223 123.132 159.63C108.531 242.438 163.823 321.404 246.631 336.005C329.439 350.606 408.405 295.314 423.006 212.506ZM273.069 18.3181C365.714 18.3181 440.819 93.4224 440.819 186.068C440.819 278.714 365.714 353.818 273.069 353.818C180.423 353.818 105.319 278.714 105.319 186.068C105.319 93.4224 180.423 18.3181 273.069 18.3181ZM441.319 186.068C441.319 93.1462 365.99 17.8181 273.069 17.8181C180.147 17.8181 104.819 93.1462 104.819 186.068C104.819 278.99 180.147 354.318 273.069 354.318C365.99 354.318 441.319 278.99 441.319 186.068ZM241.161 5.1097C341.102 -12.5125 436.405 54.2197 454.027 154.16C471.65 254.101 404.917 349.404 304.977 367.027C205.036 384.649 109.733 317.917 92.1106 217.976C74.4884 118.035 141.221 22.7319 241.161 5.1097ZM454.52 154.073C436.85 53.8609 341.287 -13.0529 241.074 4.61729C140.862 22.2875 73.948 117.85 91.6182 218.063C109.288 318.275 204.851 385.189 305.064 367.519C405.276 349.849 472.19 254.286 454.52 154.073ZM204.75 -1.63548C308.416 -39.3668 423.041 14.0838 460.773 117.75C498.504 221.415 445.053 336.04 341.387 373.772C237.722 411.503 123.097 358.052 85.3653 254.387C47.634 150.721 101.085 36.0958 204.75 -1.63548ZM461.242 117.579C423.417 13.6533 308.505 -39.9311 204.579 -2.10533C100.654 35.7204 47.0697 150.632 84.8954 254.558C122.721 358.483 237.633 412.067 341.558 374.242C445.484 336.416 499.068 221.504 461.242 117.579ZM165.194 -0.776855C268.385 -60.3546 400.336 -24.9985 459.914 78.1931C519.491 181.385 484.135 313.335 380.944 372.913C277.752 432.491 145.801 397.135 86.2236 293.943C26.6459 190.751 62.0019 58.8008 165.194 -0.776855ZM460.346 77.9431C400.631 -25.4877 268.374 -60.9256 164.944 -1.20987C61.5128 58.5059 26.0748 190.762 85.7906 294.193C145.506 397.624 277.763 433.062 381.194 373.346C484.624 313.63 520.062 181.374 460.346 77.9431ZM124.102 8.53737C222.15 -73.7343 368.328 -60.9454 450.599 37.1021C532.871 135.15 520.082 281.327 422.034 363.599C323.987 445.871 177.809 433.082 95.5377 335.034C13.266 236.987 26.0549 90.809 124.102 8.53737ZM450.982 36.7807C368.533 -61.4783 222.04 -74.2948 123.781 8.15434C25.522 90.6035 12.7055 237.096 95.1546 335.356C177.604 433.615 324.097 446.431 422.356 363.982C520.615 281.533 533.431 135.04 450.982 36.7807ZM83.2808 26.8175C171.232 -77.9993 327.502 -91.6711 432.319 -3.71941C537.136 84.2323 550.807 240.502 462.856 345.319C374.904 450.135 218.634 463.807 113.818 375.856C9.0009 287.904 -4.67093 131.634 83.2808 26.8175ZM432.64 -4.10243C327.612 -92.2316 171.027 -78.5322 82.8978 26.4961C-5.23145 131.524 8.46797 288.109 113.496 376.239C218.525 464.368 375.11 450.668 463.239 345.64C551.368 240.612 537.669 84.0268 432.64 -4.10243ZM44.6546 54.1931C117.487 -71.9566 278.794 -115.179 404.944 -42.3461C531.093 30.4865 574.316 191.793 501.483 317.943C428.65 444.093 267.343 487.315 141.194 414.482C15.0441 341.65 -28.178 180.343 44.6546 54.1931ZM405.194 -42.7791C278.805 -115.75 117.192 -72.4457 44.2215 53.9431C-28.7491 180.332 14.5549 341.945 140.944 414.915C267.333 487.886 428.945 444.582 501.916 318.193C574.887 191.804 531.583 30.1915 405.194 -42.7791ZM10.1899 90.388C63.0326 -54.7961 223.565 -129.654 368.749 -76.8109C513.933 -23.9682 588.791 136.564 535.948 281.748C483.105 426.932 322.573 501.79 177.389 448.947C32.2047 396.104 -42.6528 235.572 10.1899 90.388ZM368.92 -77.2807C223.477 -130.218 62.6572 -55.2266 9.72008 90.217C-43.217 235.661 31.7742 396.48 177.218 449.417C322.661 502.354 483.481 427.363 536.418 281.919C589.355 136.476 514.364 -24.3436 368.92 -77.2807ZM-18.188 134.712C10.1754 -26.1451 163.569 -133.552 324.425 -105.189C485.282 -76.8254 592.689 76.5678 564.326 237.425C535.962 398.281 382.569 505.688 221.712 477.325C60.8557 448.962 -46.5514 295.568 -18.188 134.712ZM324.512 -105.681C163.383 -134.093 9.7309 -26.5038 -18.6804 134.625C-47.0918 295.754 60.4969 449.406 221.626 477.817C382.754 506.229 536.407 398.64 564.818 237.511C593.23 76.3827 485.641 -77.2699 324.512 -105.681ZM-38.6814 186.068C-38.6814 13.8934 100.894 -125.682 273.069 -125.682C445.243 -125.682 584.819 13.8934 584.819 186.068C584.819 358.243 445.243 497.818 273.069 497.818C100.894 497.818 -38.6814 358.243 -38.6814 186.068ZM273.069 -126.182C100.618 -126.182 -39.1814 13.6172 -39.1814 186.068C-39.1814 358.519 100.618 498.318 273.069 498.318C445.519 498.318 585.319 358.519 585.319 186.068C585.319 13.6172 445.519 -126.182 273.069 -126.182ZM-49.7021 242.981C-81.1344 64.72 37.8941 -105.27 216.155 -136.703C394.417 -168.135 564.407 -49.1064 595.839 129.155C627.272 307.416 508.243 477.407 329.982 508.839C151.72 540.271 -18.2698 421.243 -49.7021 242.981ZM216.069 -137.195C37.5353 -105.715 -81.6747 64.5349 -50.1945 243.068C-18.7143 421.602 151.535 540.812 330.069 509.331C508.602 477.851 627.812 307.602 596.332 129.068C564.852 -49.4652 394.602 -168.675 216.069 -137.195ZM-49.9508 303.638C-114.883 125.239 -22.8995 -72.0194 155.499 -136.951C333.898 -201.883 531.156 -109.9 596.088 68.4987C661.02 246.897 569.037 444.156 390.638 509.087C212.239 574.019 14.981 482.036 -49.9508 303.638ZM155.328 -137.421C-23.33 -72.3948 -115.447 125.15 -50.4206 303.809C14.6056 482.467 212.151 574.584 390.809 509.557C569.467 444.531 661.584 246.986 596.558 68.3277C531.531 -110.33 333.986 -202.447 155.328 -137.421ZM-38.4837 365.943C-137.826 193.877 -78.8718 -26.1422 93.194 -125.484C265.26 -224.827 485.279 -165.873 584.622 6.19316C683.964 178.259 625.01 398.279 452.944 497.621C280.878 596.963 60.8586 538.009 -38.4837 365.943ZM92.944 -125.917C-79.3609 -26.4372 -138.397 193.888 -38.9167 366.193C60.5636 538.498 280.889 597.534 453.194 498.054C625.499 398.573 684.535 178.248 585.055 5.94316C485.574 -166.362 265.249 -225.398 92.944 -125.917ZM-14.7728 427.596C-148.165 268.625 -127.429 31.6189 31.541 -101.773C190.511 -235.165 427.518 -214.43 560.91 -55.4593C694.302 103.511 673.566 340.517 514.596 473.909C355.626 607.301 118.619 586.566 -14.7728 427.596ZM31.2196 -102.156C-127.962 31.4133 -148.725 268.735 -15.1558 427.917C118.414 587.099 355.735 607.862 514.917 474.292C674.099 340.723 694.862 103.401 561.293 -55.7807C427.723 -214.963 190.401 -235.726 31.2196 -102.156ZM21.2561 486.166C-144.483 347.094 -166.102 99.9956 -27.0298 -65.7439C112.042 -231.483 359.141 -253.102 524.88 -114.03C690.62 25.0422 712.238 272.141 573.166 437.88C434.094 603.62 186.996 625.238 21.2561 486.166ZM-27.4128 -66.0653C-166.662 99.8857 -145.016 347.3 20.9347 486.549C186.886 625.799 434.3 604.153 573.549 438.202C712.799 272.251 691.153 24.8367 525.202 -114.413C359.251 -253.662 111.837 -232.016 -27.4128 -66.0653ZM69.1931 539.19C-125.831 426.593 -192.651 177.217 -80.0537 -17.8069C32.5433 -212.831 281.919 -279.651 476.943 -167.054C671.967 -54.4567 738.787 194.919 626.19 389.943C513.593 584.967 264.217 651.787 69.1931 539.19Z" stroke="url(#paint0_radial_10953_12484)" stroke-width="0.5"/>
              <defs>
                <radialGradient id="paint0_radial_10953_12484" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(273.068 186.068) rotate(90) scale(408.068)">
                  <stop stop-color="var(--c-slate-4)"/>
                  <stop offset="0.92" stop-color="var(--c-slate-2)"/>
                </radialGradient>
              </defs>
            </svg>""",
            class_name="shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[0] pointer-events-none",
        ),
        # Glowing
        rx.html(
            """<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240" fill="none">
              <circle cx="120" cy="120" r="120" fill="url(#paint0_radial_10953_12483)"/>
              <defs>
                <radialGradient id="paint0_radial_10953_12483" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(120 120) rotate(90) scale(120)">
                  <stop stop-color="var(--c-violet-3)"/>
                  <stop offset="1" stop-color="var(--c-slate-2)" stop-opacity="0"/>
                </radialGradient>
              </defs>
            </svg>""",
            class_name="shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[1] pointer-events-none w-[15rem] h-[15rem]",
        ),
        # Text
        rx.text(
            text,
            class_name="text-slate-12 font-md-smbold absolute bottom-10 left-10 text-balance break-words max-w-[85%]",
        ),
        # Read text
        rx.box(
            rx.text(
                "Read",
                class_name="text-slate-9 font-small]",
            ),
            rx.icon(
                tag="chevron-right",
                class_name="!text-slate-9 size-3.5 group-hover:translate-x-0.5 transition-transform duration-150",
            ),
            class_name="absolute bottom-10 right-10 items-center gap-2 desktop-only",
        ),
        href=f"/customers/{company.lower()}",
        class_name="rounded-[1.125rem] border border-solid border-slate-4 bg-slate-2 p-10 overflow-hidden relative h-[23.25rem] lg:shadow-large group",
    )


def bento_cards() -> rx.Component:
    return rx.el.section(
        # # Dell
        # card(
        #     company="dell",
        #     text="Dell is the standard for frontend hosting. Reflex keeps them shipping.",
        # ),
        # # LlamaIndex
        # card(
        #     company="llamaindex",
        #     text="To build the fastest-growing corporate card, LlamaIndex chose the fastest tool.",
        # ),
        # # Autodesk
        # card(
        #     company="autodesk",
        #     text="Autodesk switched their 1,000 person team to Reflex to move faster.",
        # ),
        # Bayesline
        card(
            company="bayesline",
            text="Reflex give Bayesline a source-of-truth across all their work.",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-1 gap-4 mx-auto w-full max-w-[69.25rem]",
    )
