return {
  {
    "neovim/nvim-lspconfig",
    opts = {
      servers = {
        texlab = {
          mason = false,
          settings = {
            texlab = {
              build = {
                executable = "xelatex",
                -- args = {},
                onSave = true,
              },
              -- rootDirectory = "..",
              forwardSearch = {
                executable = "zathura",
                -- args = {},
              },
              diagnostics = { ignoredPatterns = { "^Overfull", "^Underfull" } },
            },
          },
        },
      },
    },
  },
}
