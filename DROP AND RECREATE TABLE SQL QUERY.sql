USE [seminat]
GO

/****** Object:  Table [dbo].[programas]    Script Date: 1/16/2023 12:24:50 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[programas]') AND type in (N'U'))
DROP TABLE [dbo].[programas]
GO

/****** Object:  Table [dbo].[programas]    Script Date: 1/16/2023 12:24:50 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[programas](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Programas] [varchar](500) NULL,
	[Universidad] [varchar](25) NULL,
	[Duracion] [varchar](25) NULL,
	[Precio] [varchar](50) NULL,
	[Tipo] [varchar](25) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


